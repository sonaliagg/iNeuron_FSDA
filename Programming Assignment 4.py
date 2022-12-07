#!/usr/bin/env python
# coding: utf-8
Programming Assignment 4
1. Write a Python Program to Find the Factorial of a Number?
# In[3]:


num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial *i
   print("The factorial of",num,"is",factorial)

2. Write a Python Program to Display the multiplication Table?
# In[5]:


num = int(input("Display multiplication table of? "))

for i in range(1, 11):
    
   print(num, 'x', i, '=', num * i)

3. Write a Python Program to Print the Fibonacci sequence?

# In[10]:


a = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

if a <= 0:
   print("Please enter a positive integer")

elif a == 1:
   print("Fibonacci sequence upto",a,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < a:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

4. Write a Python Program to Check Armstrong Number?
# In[17]:


num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

5. Write a Python Program to Find Armstrong Number in an Interval?
# In[29]:


lower = int(input("Enter the lower number:" ))
upper = int(input("Enter the upper number:" ))


for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

6. Write a Python Program to Find the Sum of Natural Numbers?
# In[35]:


n= int(input("Enter Natural Number: "))

sum= n*(n+1)/2

print("Sum of natural number is", sum)

