#!/usr/bin/env python
# coding: utf-8
 Python Basic Programming Assignment 81. Write a Python Program to Add Two Matrices?
# In[29]:


One = []
print("Enter 9 Elements for First Matrix: ")
for i in range(3):
    One.append([])
    for j in range(3):
        num = int(input())
        One[i].append(num)

Two = []
print("Enter 9 Elements for Second Matrix: ")
for i in range(3):
    Two.append([])
    for j in range(3):
        num = int(input())
        Two[i].append(num)

Three = []
for i in range(3):
    Three.append([])
    for j in range(3):
        Three[i].append(One[i][j]+Two[i][j])

print("Addition Result of Two Given Matrix is:")
for i in range(3):
    for j in range(3):
        print(Three[i][j], end=" ")
    print()

2. Write a Python Program to Multiply Two Matrices?
# In[2]:


matOne = []
print("Enter 9 Elements for First Matrix: ")
for i in range(3):
    matOne.append([])
    for j in range(3):
        num = int(input())
        matOne[i].append(num)

matTwo = []
print("Enter 9 Elements for Second Matrix: ")
for i in range(3):
    matTwo.append([])
    for j in range(3):
        num = int(input())
        matTwo[i].append(num)

matThree = []
for i in range(3):
    matThree.append([])
    for j in range(3):
        matThree[i].append(matOne[i][j] * matTwo[i][j])

print("\nAddition Result of Two Given Matrix is:")
for i in range(3):
    for j in range(3):
        print(matThree[i][j], end=" ")
    print()

3. Write a Python Program to Transpose a Matrix?
# In[28]:


One = []
print("Enter 9 Elements for Matrix: ")
for i in range(3):
    One.append([])
    for j in range(3):
        num = int(input())
        One[i].append(num)
        
Three = []
for i in range(3):
    Three.append([])
    for j in range(3):
         Three[i].append(One[i][j])

print("Transpose of Matrix is:")
for i in range(3):
    for j in range(3):
        print(Three[j][i], end=" ")
    print()

4. Write a Python Program to Sort Words in Alphabetic Order?

# In[26]:


my_str = input("Enter a string: ")

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
   print(word)

5. Write a Python Program to Remove Punctuation From a String?
# In[32]:


punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punc:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

