#!/usr/bin/env python
# coding: utf-8

# In[3]:


n= int(input('enter any number to find the fibonacci series:'))
a= 0
b= 1
if n == 1:
    print(a)
else:
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        if c<n :
            print(c)
        

