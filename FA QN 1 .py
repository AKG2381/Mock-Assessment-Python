#!/usr/bin/env python
# coding: utf-8

# ## Python - 01
# 
# ### Q2. You will be given a list. You have to print a list whose 1st element should be largest and 2nd should be the smallest then the 3rd should be 2nd largest and 4th should be 2nd smallest and so on.
# 
# #### Input Format:
# 
# ##### The first line will have space-separated elements of the list.
# 
# #### Output Format:
# 
# ##### Print the required list.
# 
# > Sample Input 0:
# 
# >1 2 3 4 5 6
# 
# > Sample Output 0:
# 
# >6 1 5 2 4 3
# 
# 

# In[1]:


l = list(map(int, input().split()))
l1= []
l.sort()
for i in range(len(l)):
    if i%2 == 0:
        x = l.pop()
        l1.append(x)
    elif i%2 != 0:
        y = l.pop(0)
        l1.append(y)
print(l1)


# In[ ]:




