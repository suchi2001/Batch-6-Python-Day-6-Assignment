#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Question:1")


# In[2]:


print("Convert to a dicitionary in one line code using list comprehension (without using zip method)")


# In[7]:


# Python3 code to demonstrate 
# conversion of lists to dictionary 
# using naive method 

# initializing lists 
list1 = [1,2,3,4,5,7,8] 
list2 = ["a","b","c","d","e"] 

# Printing original keys-value lists 
print ("Original key list is : " + str(list1)) 
print ("Original value list is : " + str(list2)) 

# using naive method 
# to convert lists to dictionary 
res = {} 
for key in list1: 
    for value in list2: 
        res[key] = value 
        list2.remove(value) 
        break

# Printing resultant dictionary 
print ("Resultant dictionary is : " + str(res)) 

