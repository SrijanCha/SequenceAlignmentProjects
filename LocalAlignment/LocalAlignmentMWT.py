#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import all libraries here


# In[2]:


class Node:
    
    def __init__(self, data):
        self.data = data
        self.children = []
        self.isWord = False
    


# In[3]:


def addWord(root, word):
    
    curr = root
    for char in word:
        
        found = False
        
        for child in curr.children:
            if (child.data == char):
                curr = child
                found = True
                break
        
        if not found:
            newNode = Node(char)
            curr.children.append(newNode)
            curr = newNode
            
    curr.isWord = True


# In[4]:


#Was not used
def findWord(root, word):
    
    curr = root
    for char in word:
        
        found = False
        
        for child in curr.children:
            if (child.data == char):
                curr = child
                found = True
                break
                
        if not found:
            return False
        
    return curr.isWord
        


# In[5]:


#initialize the two MWTs
mwt1 = Node(None)
dict1 = {}
mwt2 = Node(None)
dict2 = {}


# In[6]:


#construct the first MWT
infile = open('queries.txt','r')

line = infile.readline()
while line:
    line = line[:-1]
    addWord(mwt1, line)
    dict1[line] = 0
    line = infile.readline()

infile.close()


# In[7]:


#construct the second MWT
infile = open('queries2.txt','r')

line = infile.readline()
while line:
    line = line[:-1]
    addWord(mwt2, line)
    dict2[line] = 0
    line = infile.readline()

infile.close()


# In[8]:


#make a long string database
infile = open('DNA.txt','r')
db = ''

line = infile.readline()
line = infile.readline()
while line:
    line = line[:-1]
    db = db + line
    line = infile.readline()
    
infile.close()


# In[9]:


#program for query1

#start wherever in the db
start = 0

for i in range(start, len(db) - 50):
    
    #take the db in sets of 50 letters.
    substr = db[i:i+50]
    
    curr = mwt1
    currString = ''
    
    #go through each character in the substring
    for char in substr:
        found = False
        
        #if the character is in the MWT children:
        for child in curr.children:
            if (child.data == char):
                curr = child                             #traverse to the next child
                currString = currString + curr.data      #add the new letter to the working string (currString)
                found = True
                break
        
        #if the character is not in the MWT, go to the next set of 50 letters.
        if not found:
            break
        
        #if the character was in the MWT, check if it is a word node.
        if (curr.isWord):
            
            #if it is a word node, find it in the logs and increment the number of hits
            dict1[currString] += 1


# In[10]:


for key in dict1:
    print(key, dict1[key])


# In[11]:


#program for query1

#start wherever in the db
start = 0

for i in range(start, len(db) - 50):
    
    #take the db in sets of 50 letters.
    substr = db[i:i+50]
    
    curr = mwt2
    currString = ''
    
    #go through each character in the substring
    for char in substr:
        found = False
        
        #if the character is in the MWT children:
        for child in curr.children:
            if (child.data == char):
                curr = child                             #traverse to the next child
                currString = currString + curr.data      #add the new letter to the working string (currString)
                found = True
                break
        
        #if the character is not in the MWT, go to the next set of 50 letters.
        if not found:
            break
        
        #if the character was in the MWT, check if it is a word node.
        if (curr.isWord):
            
            #if it is a word node, find it in the logs and increment the number of hits
            dict2[currString] += 1


# In[12]:


for key in dict2:
    print(key, dict2[key])


# In[ ]:




