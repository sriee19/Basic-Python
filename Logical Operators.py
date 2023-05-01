#!/usr/bin/env python
# coding: utf-8

# # Logical Operators

# If applicant has high income AND good credit , They are Eligible for loan

# here we using the AND logic operator

# In[1]:


has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")


# In[3]:


has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# If applicant has high income OR good credit , They are Eligible for loan

# here we are using the OR logic operator

# In[4]:


has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# In[5]:


has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# AND : Both conditions should be true

# OR : Any one of the condition can be true

# NOT : the condition for not eligible

# If applicant has high income AND doesnot have criminal background, we use NOT condition

# In[6]:


has_high_income = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# In[7]:


has_high_income = True
has_criminal_record = True

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# In[ ]:




