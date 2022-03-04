#!/usr/bin/env python
# coding: utf-8

# # 1. Display Exception

# In[ ]:


try:
  print('Value of X')
except NameError:
  print("Variable X is not defined")
except:
  print("Something else went wrong")


# # Two user Inputs , pass those inputs.If user input 0 , then throw ZeroDivisionError Exp

# In[ ]:


try:
    x=int(input('Input 1 :'))
    y=int(input('Input 2 :'))
    print('Value of x and y ',x,y)

    if x==0 :
        raise ZeroDivisionError
    if y==0 :
        raise ZeroDivisionError
except ZeroDivisionError:
    raise ZeroDivisionError('user input x should not be zero')
    
# try:
#     x=int(input('Input 1 :'))
#     y=int(input('Input 2 :'))

 
# except ValueError:
#     raise ValueError('user input should be greater than zero')
# if (x==0 or y==0):
#     NError = ValueError('user input should be greater than zero')
#     raise NError


# # 3. Import math package ...

# In[ ]:


import math

try:
    x = math.exp(5000)
    print(x)
except OverflowError:
    x = float('inf')


# # 4. create your own exception with the help of class and functions

# In[ ]:


class CustomeExp(Exception):
 
    def __init__(self, value):
        self.value = value
 
    def __str__(self):
        return(repr(self.value)) 
    try:
        raise(CustomeExp(2+1))

    except CustomeExp as error:
        print('A New Exception occured: ',error.value)


# In[ ]:





# In[ ]:





# In[ ]:




