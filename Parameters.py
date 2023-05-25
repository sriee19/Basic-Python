#!/usr/bin/env python
# coding: utf-8

# # Parameters

# In[1]:


def greet_users():
    print('Hi!!')
    
print('Start')
greet_users()
print('Finish')


# In[2]:


#these are the functions


# In[3]:


#if we could pass the information to the functions


# In[4]:


def greet_users(name):
    
    print('Hi!!')
    
print('Start')
greet_users("san")
print('Finish')


# In[6]:


def greet_users(name):
    print(f'Welcome {name}')
    print('Hi!!')
    
print('Start')
greet_users("san")
greet_users("sri")
print('Finish')


#  since the parameter is given, argument must be given when the function is called

# In[8]:


def greet_users(name,work):
    print(f'Welcome {name} {work}')
    print('Hi!!')
    
print('Start')
greet_users("san","student")
greet_users("sri","doctor")
print('Finish')


# In[9]:


#The above given is passing 2 parameters


# # Key arguments

# In[10]:


# while passing the arguments , the position matters!!!


# In[11]:


#that is why they are reffered to positional arguments


# In[12]:


# the argument also should not contain the parameters name


# In[13]:


# If they are used they are called keyword argument


# In[14]:


def greet_users(name,work):
    print(f'Welcome {name} {work}')
    print('Hi!!')
    
print('Start')
greet_users(name="san",work="student")
print('Finish')


# # Return statement

# In[ ]:




