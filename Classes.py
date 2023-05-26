#!/usr/bin/env python
# coding: utf-8

# # Classes

# Numbers , strings , booleans are types in python

# Some are complex types like lists and dictionaries
# 

# In[1]:


# we use classes to define a new type of models


# In[2]:


class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
point1 = Point()
point1.draw()
point1.move()


# In[4]:


class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
point1 = Point()
point1.draw()
point1.move()

#we could also define point.x to some value

point1.x = 10
point1.y = 30
print(point1.y)


# In[5]:


# now we create another object

point2 = Point()
point2.x = 25
print(point2.x)
point2.draw()


# # Constructors

# In[6]:


# we could create a point object without a x or y coordinate


# In[7]:


point = Point()
print(point.x)


# In[8]:


# we would get attribute error because we have not defined a x 


# In[9]:


# to solve this we use constructor


# In[1]:


class Point:
    #we use init operator
    def __init__(self, x, y):
        #initialize our coordinates
        self.x =x
        self.y = y
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
point = Point(10,20)
print(point.x)


# In[2]:


# Define a new type PERSON and with name attribute


# In[11]:


class person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"hi i am {self.name}")
names = person("sanjana")
#print(names.name)
pavan = person("pavan")
pavan.talk()
names.talk()


# # Inheritance

# In[12]:


class Dog:
    def walk(self):
        print("walk")

class Cat:
    def walk(self):
        print("walk")
#donot define the varible twice

#to overcome this problem we inherit the two classses into a parent class 


# In[16]:


class Mammal:
    def walk(self):
        print("walking")


class Dog(Mammal): #here the dog class is inheriting from the mammal
    pass #to not have an empty class

class Cat(Mammal):
    def meow(self):  #we could also define another activity
        print("but Meows!!")

dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()
cat1.meow()


# In[ ]:




