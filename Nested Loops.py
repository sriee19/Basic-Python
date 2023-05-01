#!/usr/bin/env python
# coding: utf-8

# # Nested Loops

# here we are generating lists of co-ordinates

# In[1]:


for x in range(4):
    print(x)


# one nest for forming 2 co-ordinates

# In[6]:


for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
    ##print(x)


# # exercise

# draw the given shape using nested loops

# In[7]:


number = [5,2,5,2,2]

for item in number:
    print('*' * item)


# In[12]:


number = [5,2,5,2,2]

for item in number:
    output = ''
    for count in range(item):
        output += '*'
    print(output)
    


# In[13]:


number = [1,1,1,1,7]

for item in number:
    output = ''
    for count in range(item):
        output += '*'
    print(output)


# In[ ]:




