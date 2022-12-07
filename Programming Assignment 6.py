#!/usr/bin/env python
# coding: utf-8
Programming Basic Assignment 61. Write a Python Program to Display Fibonacci Sequence Using Recursion?
# In[18]:


n = int(input("Enter number of terms:"))

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))

2. Write a Python Program to Find Factorial of Number Using Recursion?
# In[16]:


num= int(input("Enter Number: "))

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
    
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

3. Write a Python Program to calculate your Body Mass Index?
# In[12]:


height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2
print(f"You BMI is {BMI}")
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")

4. Write a Python Program to calculate the natural logarithm of any number?
# In[8]:


import math
n = int(input("Enter Number: "))
a = math.log(n)

print("The Natural Logarithm of" ,n, "is:",a)

5. Write a Python Program for cube sum of first n natural numbers?

# In[4]:


n = int(input("Enter Natural Number: "))
Sum = ( n * (n + 1) / 2 ) ** 2
print("Cube sum of",n, "is", Sum)

