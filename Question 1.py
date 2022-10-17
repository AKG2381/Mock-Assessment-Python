#!/usr/bin/env python
# coding: utf-8

# ### Python Candidates - Question 1
# 
# ###### You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.
# 
# ######  For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be ['great', 'abc', 'hello','hiyo']
# 
# ### Input Format:
# 
# ###### At first-line it will have an integer (number of elements inside a list). In the second line, it will have a string.
# 
# ### Output Format:
# 
# ###### A single line containing a sorted list.

# In[1]:


def Question1(l):
    t=[]
    d=[i[-2] for i in l]
    d.sort()
    for i in range(len(d)):
        for j in range(len(l)):
            if d[i]==l[j][-2]:
                t.append(l[j])
    return t
n=int(input())
s=[input() for i in range(n)]
Question1(s)


# In[ ]:




