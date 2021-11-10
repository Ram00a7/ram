#!/usr/bin/env python
# coding: utf-8

# In[1]:



n = (10, 21, 4, 45, 66, 93, 1)
  
even_count, odd_count = 0, 0
  
for num in n :
    
    if num % 2 == 0:
        even_count += 1
  
    else:
        odd_count += 1
          
print("Even numbers in n : ", even_count)
print("Odd numbers in n : ", odd_count)

