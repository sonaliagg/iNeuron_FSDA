#!/usr/bin/env python
# coding: utf-8
Programming Assignment 31. Write a Python Program to Check if a Number is Positive, Negative or Zero?
# In[ ]:


num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

2. Write a Python Program to Check if a Number is Odd or Even?

# In[ ]:


num = float(input("Enter a number: "))
if num % 2 == 0:
   print("It is an even number")
else:
   print("It is an odd number")

3. Write a Python Program to Check Leap Year?

# In[6]:


Year = int(input("Enter a year: "))
 
if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
 
else:  
    print ("Given Year is not a leap Year")  

4. Write a Python Program to Check Prime Number?
# In[4]:


num = int(input("Enter an input number:"))  

if num > 1:
  
    for i in range(2, int(num/2)+1):
       
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
# In[5]:


lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




