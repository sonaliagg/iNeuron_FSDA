#!/usr/bin/env python
# coding: utf-8
Programming Assignment 2
1. Write a Python program to convert kilometers to miles?

# In[2]:


kilo = float(input("Enter speed in kilometer "))
conv_fact = 0.62137
mile = kilo * conv_fact
print("The speed in miles is",mile)

2.Write a Python program to convert Celsius to Fahrenheit?
# In[4]:


cel = float(input("Enter temperature in Celsius "))

fah= (cel * 1.8) + 32

print("The temperature in fahrenheit is", fah)

3. Write a Python program to display calendar?

# In[6]:


import calendar
a = int(input("Enter year - "))
b = int(input("Enter month - "))
print(calendar.month(a,b))

4. Write a Python program to solve quadratic equation?
# In[9]:


import cmath
a = int(input("Enter value of coefficient a "))
b = int(input("Enter value of coefficient b "))
c = int(input("Enter value of coefficient c "))

d = (b**2) - (4*a*c)

x = (-b-cmath.sqrt(d))/(2*a)
y = (-b+cmath.sqrt(d))/(2*a)

print('The roots are', x, y)

5. Write a Python program to swap two variables without temp variable?
# In[20]:


a = int(input("Enter the first value "))
b = int(input("Enter the second value "))
 
print ("\nBefore swapping- ",)
print("\nValue of first variable", a)
print("Value of second variable", b)

a, b = b, a

print ("\nAfter swapping- ")
print("\nValue of first variable", a )
print("Value of second variable", b )

