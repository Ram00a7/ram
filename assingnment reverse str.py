#!/usr/bin/env python
# coding: utf-8

# In[32]:


def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string
str = "1234abcd"
print("The reversed string is:", reverse(str)) 


# In[ ]:




