#!/usr/bin/env python
# coding: utf-8

# # If Statements

# We could check the statements based on the conditions

# The condition given below can be printed using condition statements

# if its hot 
# 	It's a hot day, drink plenty of water
# otherwise if its cold
# 	It's a cold day, wear warm clothes
# otherwise
# 	It's a Lovely day

# In[4]:


is_hot = True

if is_hot: 
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")


# In[3]:


is_hot = False

if is_hot: 
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")


# In[6]:


is_hot = False
is_cold = True

if is_hot: 
    print("It's a hot day")
    print("Drink plenty of water")


elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
   
    
    
print("Enjoy your day")


# In[8]:


is_hot = False
is_cold = False

if is_hot: 
    print("It's a hot day")
    print("Drink plenty of water")


elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
   
else:
    print("It's a lovely day")
    
print("Enjoy your day")


# # Exercise

# Price of a house is $1M, 
# 	If buyer has good credit, They need to put dowm 10%
#     Otherwise, they need to put down 20%
#     Print the down payment

# In[10]:


House_price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * House_price
else:
    down_payment = 0.2 * House_price
print(f"Down_payment :  ${down_payment} ")


# In[11]:


House_price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * House_price
else:
    down_payment = 0.2 * House_price
print(f"Down_payment :  ${down_payment} ")


# In[ ]:




