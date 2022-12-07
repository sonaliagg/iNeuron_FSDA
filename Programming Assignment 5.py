#!/usr/bin/env python
# coding: utf-8
Programming Assignment 5

1. Write a Python Program to Find LCM?
# In[17]:


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1

2. Write a Python Program to Find HCF?
# In[9]:


x =int(input("Enter the first number: "))
y =int(input("Enter the second number: "))
if x > y:
  x, y = y, x
for i in range(1,x+1):
  if x%i == 0 and y%i == 0:
    hcf = i

print("HCF of", x,"and", y,"is:",hcf)

3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
# In[11]:


dec = int(input("Enter an integer: "))
print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")

4. Write a Python Program To Find ASCII value of a character?
# In[16]:


A = input("Please enter a character: ")    
    
print ("The ASCII value of '" + A + "' is ", ord(A))  

5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
# In[1]:


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

