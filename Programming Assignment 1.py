#!/usr/bin/env python
# coding: utf-8

# ## Programming Assignment_1

# ### 1. Write a Python program to print "Hello Python"?

# In[1]:


print("Hello Python")


# ### 2. Write a Python program to do arithmetical operations addition and division.?
# 

# In[15]:


a = float(input("Enter first number "))
b = float(input("Enter second number "))
add = a + b
print('Addition', add)
sub = a - b
print('Substraction', sub)
multi = a * b
print('Multiplication', multi)
div = a / b
print('Division', div)


# ### 3. Write a Python program to find the area of a triangle?
# 

# In[14]:


a = float(input("Enter Height of Triangle "))
b = float(input("Enter Base of triangle "))
area = (a*b) * 0.5
print("Area ", area)


# ### 4. Write a Python program to swap two variables?
# 

# In[21]:


a = float(input("Enter first number "))
b = float(input("Enter second number "))
c = a
a = b
b = c

print('The value of a after swapping:', a)
print('The value of b after swapping:', b)


# ### 5. Write a Python program to generate a random number?
# 

# In[9]:


import random


# In[12]:


print(random.randint(0,100))

