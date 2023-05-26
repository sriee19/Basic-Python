#!/usr/bin/env python
# coding: utf-8

# # Modules

# In[1]:


# Modules are basically a file in python code


# In[ ]:


def lbs_to_kgs(weight):
    return weight*0.45
def kgs_to_lbs (weight):
    return weight/0.45


# In[2]:


#we can access different modules using the functions


# In[ ]:


# we could save the code in different module name converter.py
# we could access that module from the common file using import statement
import converter
#and we could use the dot operator to call the functions of the converter module


# In[ ]:


converter.lbs_to_kgs()

