#!/usr/bin/env python
# coding: utf-8

# # Type conversion

# converting a value into different values such as converting string to integer

# we have functions like 
# int()
# float()
# boolean()

# In[3]:


birth_year = input('Birth Year: ')
age = 2025 - int(birth_year)
print(age)


# type of the variable can be checked using type() function

# In[4]:


birth_year = input('Birth Year: ')
print(type(birth_year))


# # Question

# Ask a user their weight (in pounds), convert it to kilograms and print on the terminal.

# In[7]:


getweight = input ('Weight in pounds : ')
weight = float(getweight) * 0.45
print(weight)


# In[ ]:




