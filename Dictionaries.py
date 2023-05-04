#!/usr/bin/env python
# coding: utf-8

# # Dictionaries

# In[4]:


customer ={
    "name" : "srisanjana",
    "age" : 21,
    "is_verified" : True
}
customer["age"]


# In[6]:


print(customer["name"])


# In[7]:


print(customer.get("date"))


# In[8]:


print(customer.get("name"))


# In[9]:


print(customer.get("age"))


# In[10]:


print(customer.get("date","12.02.2022"))


# In[11]:


customer["name"] = "pavanshree"


# In[12]:


print(customer.get("name"))


# In[13]:


customer["date"] = "12.03.1972"


# In[15]:


print(customer.get("date"))


# EXERCISE

# program which asks the phone number and translate it to english

# In[3]:


Phone = input("Phone:  ")

# mapping the numbers to the key
# "1" --> "one"
# "2" --> "two"

# creating the dictionary

digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output = ""
for ch in Phone:
    output += digits_mapping.get(ch , "!") + "  "
print(output)    


# In[4]:


Phone = input("Phone:  ")

# mapping the numbers to the key
# "1" --> "one"
# "2" --> "two"

# creating the dictionary

digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output = ""
for ch in Phone:
    output += digits_mapping.get(ch , "!") + "  "
print(output)    


# In[ ]:




