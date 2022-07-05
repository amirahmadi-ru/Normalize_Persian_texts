#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[4]:


i = input()

def normalize_spaces(i):
#     i = i.replace("\n", " ").replace("\t", " ")
#     i = re.sub('\n*',' ',i)
    i = re.sub('  *',' ',i)
    i = re.sub('   *',' ',i)
    i = re.sub('    *',' ',i)
    return i
    
normalize_spaces(i)

