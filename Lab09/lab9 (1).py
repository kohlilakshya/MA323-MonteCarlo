import numpy as np
import time
import scipy.stats as stats
import random as random
import seaborn as sns
import matplotlib.pyplot as plt

import math

np.random.seed(42)

Task_mean = np.array([4,4,2,5,2,3,2,3,2,2]) 


# For this question
# E1= T1 
# E2= T1+ T2
# E3= T1 + T3
# E4= T1 + T2 + T4
# E5= T1 + T2 + T5
# E6 = T1 + T3 + T6
# E7= T1 + T3 + T7 
# E8= T1 + T3 + T8
# E9= T1 + T9 +max{ T2 + T5, T3 + T6, T3 + T7}
# E10 = T1 + T10 + max{T2 + T4, T3 + T8 , T9 + max {T2 + T5, T3 + T6, T3 + T7} }

def generate_diff_exponential(mean):
    
    
    U= np.random.uniform()
    X= -mean * math.log(1-U)
    
    return X    



def fx(mean,x):
    return 1/mean * (math.pow(math.e,-x/mean))

def qx(mean,x,k):
    mean=mean*k
    return 1/mean * (math.pow(math.e,-x/mean))
    
def expected_mean(total, Task_mean):
    
    E10_list = np.empty(total)
    count = 0
    
    for j in range(total):
        
        
        Task_samples = np.empty(Task_mean.size)
        
        
        
        for i in range(Task_mean.size):
            
            Task_samples[i] = generate_diff_exponential(Task_mean[i])
    
    
    
        term1 = Task_samples[9] + Task_samples[0]
        term2 = max(Task_samples[1] + Task_samples[3], Task_samples[2] + Task_samples[7])
        term3 = Task_samples[8] + max(Task_samples[1] + Task_samples[4], 
                                        Task_samples[2] + Task_samples[6], 
                                        Task_samples[2] + Task_samples[5])
        
        E10_list[j] = term1 + max(term2, term3)
        
        if(E10_list[j] >= 70 ):
            count+=1

    mean = np.mean(E10_list)
    variance = np.std(E10_list)**2
    probab= count/total
    
    
    
    

    return E10_list,mean, variance,probab,count

# Example usage:
# mean, var = expected_mean(10000, Task_mean)

def expected_mean_with_important_sampling(total, Task_mean,k,condition):
    
    E10_list = np.empty(total)
    count_list= np.empty(total)
    expected_sample_size= np.empty(total)
    count = 0
    
    
    for j in range(total):
        
        
        Task_samples_forp = np.empty(Task_mean.size)
        Task_samples_forq = np.empty(Task_mean.size)
        
        
        if(condition==False):
            for i in range(Task_mean.size):
                
                
                Task_samples_forp[i] = generate_diff_exponential(Task_mean[i]) 
                Task_samples_forq[i] = generate_diff_exponential(k * Task_mean[i]) 
            
        
        else:
            
            for i in range(Task_mean.size):
                
                
                Task_samples_forp[i] = generate_diff_exponential(Task_mean[i]) 
                
                if(i==0 or i==1 or i==3 or i==9):
                    
                    Task_samples_forq[i] = generate_diff_exponential(k * Task_mean[i]) 
            
                else:
                    Task_samples_forq[i] = generate_diff_exponential(Task_mean[i])
                    
             
            
           
        
        
        term1 = Task_samples_forq[9] + Task_samples_forq[0]
        term2 = max(Task_samples_forq[1] + Task_samples_forq[3], Task_samples_forq[2] + Task_samples_forq[7])
        term3 = Task_samples_forq[8] + max(Task_samples_forq[1] + Task_samples_forq[4], 
                                        Task_samples_forq[2] + Task_samples_forq[6], 
                                        Task_samples_forq[2] + Task_samples_forq[5])
        
        E10_list[j] = term1 + max(term2, term3)
        
        if(condition==False):
            for i in range(Task_mean.size):
                Task_samples_forp[i] = 1/Task_mean[i] *(math.pow(math.e,-Task_samples_forq[i]/Task_mean[i]))
                Task_samples_forq[i] = 1/(k*Task_mean[i]) *(math.pow(math.e,-Task_samples_forq[i]/(k*Task_mean[i])))
            
        else:
            for i in range(Task_mean.size):
                Task_samples_forp[i] = 1/Task_mean[i] *(math.pow(math.e,-Task_samples_forq[i]/Task_mean[i]))
                if(i==0 or i==1 or i==3 or i==9):
                    
                    Task_samples_forq[i] = 1/(k*Task_mean[i]) *(math.pow(math.e,-Task_samples_forq[i]/(k*Task_mean[i])))
                
                else:
                    Task_samples_forq[i] = 1/(Task_mean[i]) *(math.pow(math.e,-Task_samples_forq[i]/(Task_mean[i])))
                
                    
            
        if(E10_list[j] >= 70 ):
            count_list[j]=np.prod(Task_samples_forp)/np.prod(Task_samples_forq)
            expected_sample_size[j]=count_list[j]
            
            count+= np.prod(Task_samples_forp)/np.prod(Task_samples_forq)
        else:
            count_list[j]=0
            expected_sample_size[j]=np.prod(Task_samples_forp)/np.prod(Task_samples_forq)
            
            
    mean = np.mean(E10_list)
    
    variance_forE10 = np.std(E10_list)**2
    probab= count/total
  
    variance_forcount= math.pow(np.std(count_list),2)
    
    summation= np.sum(expected_sample_size)
    sqsum= np.sum(np.power(expected_sample_size,2))
    
    
    
    
    
    return E10_list,mean, variance_forE10,probab,variance_forcount,summation*summation/sqsum

    


    




    
E10_list,mean,var,probab,count= expected_mean(1000000,Task_mean)
E10_list2,mean2,var2,probab2,var2_forcount,expected_sample_size=expected_mean_with_important_sampling(1000000,Task_mean,4,False)


print("***************************** Q1 B part  *************************")
print(f"E10 list is {E10_list}")
print("\n")
print(f"Sample mean of E10 that I got is {mean}")


print("***************************** Q1 C part  *************************")

plt.title("Histplot for E10")
sns.histplot(E10_list)
plt.show()


print("***************************** Q1 d part  *************************")


print(f"Approximate probablity that the project will miss the deadline is {probab}")

print(f"standard deviation that I got for n=1000000 is {math.sqrt(var)}")


print("***************************** Q1 E part  *************************")


print(f"Here mean of E10 that I got is {mean2}")

print(f"Here sample standard deviation  that I got is approximately {math.sqrt(var2_forcount)}")

print(f"Here Expected Sample size that I got is approximately {expected_sample_size}")


print("***************************** Q1 F part  *************************")



E10_list1,mean1,var1,probab1,var1_forcount,expected_sample_size1=expected_mean_with_important_sampling(1000000,Task_mean,3,True)
E10_list2,mean2,var2,probab2,var2_forcount,expected_sample_size2=expected_mean_with_important_sampling(1000000,Task_mean,4,True)
E10_list3,mean3,var3,probab3,var3_forcount,expected_sample_size3=expected_mean_with_important_sampling(1000000,Task_mean,5,True)
print(f"For k=3  probablity  that I got is approximately {probab1}")
print(f"For k=3  sample standard deviation that I got is approximately {math.sqrt(var1_forcount)}")
print(f"Here Expected Sample size that I got is approximately {expected_sample_size1}")
print(f"For k=4  probablity  that I got is approximately {probab2}")
print(f"For k=4  sample standard deviation that I got is approximately {math.sqrt(var2_forcount)}")
print(f"For k=4 Expected Sample size that I got is approximately {expected_sample_size2}")
print(f"For k=5  probablity  that I got is approximately {probab3}")
print(f"For k=5 sample standard deviation that I got is approximately {math.sqrt(var3_forcount)}")
print(f" For k=5 Expected Sample size that I got is approximately {expected_sample_size3}")


print("***************************** Q1 H part  *************************")


print(f"For k=3  99%  Confidence Interval That I got is {probab1- 2.58*math.sqrt(var1_forcount/1000000)} - {probab1+ 2.58*math.sqrt(var1_forcount/1000000)}")

print(f"For k=4  99%  Confidence Interval That I got is {probab2- 2.58*math.sqrt(var2_forcount/1000000)} - {probab2+ 2.58*math.sqrt(var2_forcount/1000000)}")


print(f"For k=5  99%  Confidence Interval That I got is {probab3- 2.58*math.sqrt(var3_forcount/1000000)} - {probab3+ 2.58*math.sqrt(var3_forcount/1000000)}")