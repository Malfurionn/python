#!/usr/bin/env python
# coding: utf-8

# In[16]:


def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1


# In[17]:


while True:
    try:
        i = int(input("Enter a number:\n"))
        break
    except ValueError:
        print("You should enter an integer.")
        continue
while i != 1:
    i = collatz(i)
    print(i)


# In[ ]:




