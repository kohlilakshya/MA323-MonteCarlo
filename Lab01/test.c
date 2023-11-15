#include <stdio.h>
int main()
{
    int a[10];
    for (int i = 0; i < 20; i++)
    {
        if (i < 10)
            a[i] = 20;
        else
            a[i] = 50;
    }
    int *ptr = a;
    printf("%p\n", ptr);

    printf("%d\n", *(ptr +9));

    // for (int i = 0; i < 20; i++)
    // {
    //     printf("%d %d\n", a[i], i);
    // }
}