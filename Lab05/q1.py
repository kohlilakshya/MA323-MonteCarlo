import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import math


def box_muller(n):
    z1 = list()
    for i in range(n):
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)
        r = math.pow(-2*np.log(u1), 1/2)
        theta = 2*np.pi*u2
        t = r*np.sin(theta)
        z1.append(t)
    return z1

a_values = [-.5, 0,.5,1]
for a in a_values:
    mean = np.array([5,8])
    covariance = np.array([[1, 2*a], [2*a,4]])
    sigma1 = np.sqrt(covariance[0][0])
    mu1 = mean[0]
    sigma2 = np.sqrt(covariance[1][1])
    mu2 = mean[1]
    rho = 2*a/(sigma1*sigma2)

    z1 = box_muller(10000)
    z2 = box_muller(10000)
    x1 = list()
    x2 = list()
    for i in range(10000):
        x1.append(mu1 + sigma1*z1[i])
        x2.append(mu2 + rho*sigma2*z1[i] + np.sqrt(1-rho*rho)*sigma2*z2[i])

    title = f"a={a}"
    layout = go.Layout(
    title=title,
    xaxis=dict(title="X1-axis Label"),
    yaxis=dict(title="X2-axis Label"),     
    )
    
    fig = go.Figure(go.Histogram2d(x=x1, y = x2), layout=layout)
    fig.show()
    X = np.random.multivariate_normal(mean, covariance, 10000).T

    fig = go.Figure(go.Histogram2dContour(x=X[0], y = X[1]), layout=layout)
    fig.show()