#!/usr/bin/env python
# coding: utf-8

# In[13]:


def core(result):
    bigWord = None
    bigCount = None
    
    for word,count in result.items():
        if bigWord is None or count > bigCount:
            bigWord = word
            bigCount = count
            
    print("\nMost Typed Word in the given file is =>  ",end="")
    print(bigWord)
    print("Frequency of Word = ", end ="")
    print(bigCount)

print("########## MOST TYPED WORD COUNTER & IDENTIFIER ########## \nDeveloper: Hardik Agarwal, 17CE015")

try:
    choice = int(input("Enter Your Choice \n 1. File Path \n 2. Input Data \n\n"))    
except:
    print("Invalid Choice")

result = {}
if choice == 1:
    try:
        path = input("Enter File Path: \n")
    except:
        print("Invalid Path")
    
    handle = open(path)
    
    for line in handle:
        words = line.split()
        for word in words:
            result[word] = result.get(word, 0) + 1
    core(result)
            

elif choice == 2:
    data = input("Enter String \n")
    words = data.split()
    
    for word in words:
        result[word] = result.get(word,0) + 1
        
    core(result)

