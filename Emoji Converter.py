#!/usr/bin/env python
# coding: utf-8

# # Emoji Converter

# In[4]:


print("good morning :)")


# to get the emoji we use the following code

# In[6]:


message = input("> ")
words = message.split(' ')
print(words)


# The spilt function divides each string to a division

# To map the special character to emojies

# In[8]:


message = input("> ")
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "☹️"
}
output = " "
for word in words:
    output += emojis.get(word,word) + " "
print(output)


# In[9]:


message = input("> ")
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "☹️"
}
output = " "
for word in words:
    output += emojis.get(word,word) + " "
print(output)


# In[ ]:




