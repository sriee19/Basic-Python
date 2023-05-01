#!/usr/bin/env python
# coding: utf-8

# # Comparison Operators

# if temperature is greater than 30, it's a hot day..///otherwise if it's less than 10, it's a cold day /// otherwise  it's neither hot nor cold

# In[1]:


temperature = 30

if temperature > 30:
    print("it's a hot day")
else:
    print("It's not a hot day")


# In[2]:


temperature = 39

if temperature > 30:
    print("it's a hot day")
else:
    print("It's not a hot day")


# In[3]:


temperature = 30

if temperature >= 30:
    print("it's a hot day")
else:
    print("It's not a hot day")


# In[4]:


temperature = 30

if temperature < 30:
    print("it's a hot day")
else:
    print("It's not a hot day")


# In[5]:


temperature = 30

if temperature <= 30:
    print("it's a hot day")
else:
    print("It's not a hot day")


# In[6]:


temperature = 30

if temperature == 30:
    print("it's a hot day")
else:
    print("It's not a hot day")


# In[7]:


temperature = 30

if temperature != 30:
    print("it's a hot day")
else:
    print("It's not a hot day")


# If name is less than 3 characters long , name must be atleast 3 characters////otherwise if it's more tham 50 characters long , name can be maximum of 50 characters//// otherwise , name looks good!!!

# In[11]:


name = 'srisanjana'

if len(name) < 3:
    print("name must be atleast 3 characters long")
elif len(name)>50:
    print("name must be maximum of 50 chracters")
else:
    print("name looks good!")


# In[ ]:




