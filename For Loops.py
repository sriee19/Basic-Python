#!/usr/bin/env python
# coding: utf-8

# # For Loops
# 

# In[1]:


## syntax
## for variable in 'string':


# In[3]:


for item in [ 'san', 'jana' , 'pavan']:
	print(item)


# In[4]:


for item in [1,2,3,4]:
	print(item)


# In[6]:


for item in range(5,10):
    print(item)
## start range 


# In[7]:


for item in range(5,10,2):
    print(item)
## adding steps counts


# In[9]:


prices = [10,20,30]
total = 0

for item in prices:
    total += item
print(total)


# In[ ]:




