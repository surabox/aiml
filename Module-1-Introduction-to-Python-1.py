#!/usr/bin/env python
# coding: utf-8

# # Module-1-Introduction-to-Python-Assignment-1

# # 1. Create a list containing squares of numbers from 1 to 10 (HINT: use List Comprehension).

# In[ ]:


numbers= list(range(1,11))

sq_numbers=[i*2 for i in numbers]

print(sq_numbers)


# # 2. Write a Function to check if year number is a leap year.

# In[ ]:


def CheckLeapYear(year) :
    if(((year % 400 ==0) or (year % 100 ==0)) and (year % 4==0)):
        print('Input year is a leap year')
    else:
        print('Input year is not a leap year')

enter_year=int(input('Enter the year : '))
CheckLeapYear(enter_year)
    


# # 3. Write a Function to take an array and return another array that contains the members of first array that are even

# In[ ]:


import array as arr
listOfNos=[*range(1,100)]

a=arr.array('i',listOfNos)
listEvenNos=[]

for x in (a):
    if (x%2)==0:
        listEvenNos+=[x]     
print(listEvenNos)


# In[2]:


array1=[1,2,3,44,53,656,23,255,2524,24664,667]

array2EvenNos=[]

for x in (array1):
    if (x%2)==0:
        array2EvenNos+=[x]     
print(array2EvenNos)


# # 4. Write a Function that takes 2 arrays and prints the members of first array that are present of second array. (HINT: use Membership Comprehension)

# In[8]:


def arrayOfNos(arr1,arr2):
    for x in arr1:
        if x in arr2 :
            print('Element present in prent in 1st array :',x)
        
arr1=[1,2,3,44,53,656,23,255,2524,24664,667]
arr2=[1,2,33,441,53,656,237,255,2524,1,5]

arrayOfNos(arr1,arr2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




