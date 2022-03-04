#!/usr/bin/env python
# coding: utf-8

# # 1. Create 1st tuple with values -> (10,20,30), 2nd tuple with values -> (40,50,60).
# 

# # a. Concatenate the two tuples and store it in “t_combine”

# In[1]:


t1= (10,20,30)
t2= (40,50,60)
t_combine=t1+t2;
print(t_combine)


# # Repeat the elements of “t_combine” 3 times

# In[2]:


t_combine_3_times=(t_combine * 3)
print(t_combine_3_times)


# # Access the 3rd element from “t_combine”

# In[3]:


print(t_combine[2])


# # Access the first three elements from “t_combine”

# In[4]:


print(t_combine[0:3])


#  # Access the last three elements from “t_combine”

# In[5]:


print(t_combine[-3:])


# # 2. Create a list ‘my_list’ with these elements:

# # a. First element is a tuple with values 1,2,3 , b. Second element is a tuple with values “a”,”b”,”c”, c. Third element is a tuple with values True,False

# In[6]:


my_list=[[(1,2,3)] , [('a','b','c')] , [(True,False)]]
print(my_list)


# # 3. Append a new tuple – (1,’a’,True) to ‘my_list’

# In[7]:


my_list.append((1,'a',True))
print(my_list)


# # 4. Create a dictionary ‘fruit’ where: a. The first key is ‘Fruit’ and the values are (“Apple”,”Banana”,”Mango”,”Guava”) b. The second key is ‘Cost’ and the values are (85,54,120,70) c. Extract all the keys from ‘fruit’ d. Extract all the values from ‘fruit’

# In[8]:


fruitDic={'Fruit':['Apple','Banana','Mango','Guava'] , 'Cost' : [85,54,120,70]}
print(fruitDic.keys())
print(fruitDic.values())


# # 5. Crete a set named ‘my_set’ with values (1,1,”a”,”a”,True,True) and print the result

# In[9]:


my_set={1,1,'a','a',True,True}

for x in my_set:
    print(x)

