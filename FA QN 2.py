#!/usr/bin/env python
# coding: utf-8

# # Python - 02
# ## QN 2Find nth fibonacci number. If it starts with 0,1,1,2.....
# 
# ## Also, Print Incorrect Input if n is less than or equal to 0.
# 
# ### Input Format:
# 
# #### Call the function with n
# 
# ### Output Format:
# 
# #### Print the nth fibonacci number
# 
# >Sample Input 0:
# 
# >4
# 
# >Sample Output 0:
# 
# >2
# 
# >Sample Input 1:
# 
# > 0
# 
# >Sample Output 1:
# 
# >Incorrect input

# In[37]:


n=int(input())
l=[0,1]
if n==0:
    print("Incorrect input")
elif n==1:
    print(l[0])
else:
    for i in range(n-2):
        l.append(l[i]+l[i+1])
    print(l.pop())
            
      
     


# In[ ]:





# In[ ]:




