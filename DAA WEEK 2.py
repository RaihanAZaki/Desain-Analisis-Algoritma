#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np


# In[26]:


print(np.__version__)
#Cek Versi Python


# In[3]:


print("Hello World")
#Print HelloWorld


# In[27]:


print("Nama saya (Raihan)")
#Print Nama


# In[5]:


print("NIM saya (2020071037)")
#Print NIM


# In[6]:


if 5>2:
    print ("Five is greater than two!")
#Print if


# In[28]:


x = 5
y = ("john")
print (x)
print (y)
#Print var x dan var y

x = 4
x = ("Sally")
print (x)
#Print x mengapa Sally karena nilai "4" telah tertimpa oleh x = "Sally"


# In[8]:


def getFirst(myList):
    return myList[0]
getFirst([1,2,3])
#Print angka pertama 


# In[9]:


def getSecond(myList):
    return myList[1]
getSecond([1,2,3])
#Print angka kedua


# In[29]:


def getLast(myList):
    return myList[-1]
getLast([1,2,3])
#Print angka terakhir


# In[2]:


def getSum(myList):
    sum = 0
    for item in myList:
        sum = sum+item
    return sum
getSum([1,2,3])
#Sum penjumlahan


# In[4]:


def getKali(myList):
    sum = 1
    for item in myList:
        sum = sum*item
    return sum
getKali([1,2,3,4])
#Sum perkalian


# In[6]:


def getBagi(myList):
    sum = 100
    for item in myList:
        sum = sum/item
    return sum
getBagi([10,5,1])
#Sum pembagian


# In[8]:


def getSum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum += item
    return sum
getSum ([[1,2,5],[3,4,7]])
#getSum ([[1,2],[3,4]])
#getSum ([[1,2,3],[4,5,6]])

#Penjumlahan 2 himpunan angka


# In[30]:


def getBagi(myList):
    sum = 1
    for row in myList:
        for item in row:
                sum /= item
    return sum
getBagi([[1,2,3],[4,5,6]])

#Pembagian 2 himpunan angka


# In[36]:


def getPengurangan(myList):
    sum = 50
    for row in myList:
        for item in row:
            sum -= item
    return sum
getPengurangan([[1,2,3],[4,5,6]])

#Pengurangan 2 himpunan angka


# In[22]:


def searchBinary(myList,item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while( first<=last and not foundFlag):
        mid = (first + last) //2
        if myList[mid] == item :
            foundFlag = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag
#searchBinary ([8,9,10,100,1000,2000,3000], 10)
searchBinary ([8,9,10,100,1000,2000,3000], 5)

#Mencari binary dengan jawaban "True" or "False"


# In[ ]:




