#!/usr/bin/env python
# coding: utf-8

# # While loops

# Building simple game using while loops

# In[1]:


#### syntax
## while condition: and a block which needs to be printed


# In[2]:


i = 5
while i<=10:
    print(i)
    i = i + 1
print("Done")


# In[5]:


i = 1
while i<=5:
    print('*' * i)
    i = i + 1
print("#################")


# # Guessing game

# The guess game is played by making the user guess any number 
# and finding the hidden number...//// we are gonna build this game using while loop

# In[9]:


secret_num = 9
num_guess = 0
guess_limit = 3
while num_guess < guess_limit:
    Guess = int(input('Guess:  '))
    num_guess += 1
    if Guess == secret_num:
        print('You Win!')

    


# In[14]:


secret_num = 9
num_guess = 0
guess_limit = 3
while num_guess < guess_limit:
    Guess = int(input('Guess:  '))
    num_guess += 1
    if Guess == secret_num:
        print('You Win!')
        break
    else:
        print("Guess Again")
else:
    print("You failed :(")


# In[ ]:




