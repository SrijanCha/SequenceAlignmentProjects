#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import argparse


# In[4]:


def generateRandomSeq(length):
    nums = np.random.randint(0, 4, length)
    seq = ''
    
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    
    
    for num in nums:
        if(num == 0):
            seq += 'A'
            count1 += 1
        elif(num == 1):
            seq += 'C'
            count2 += 1
        elif(num == 2):
            seq += 'G'
            count3 += 1
        elif(num == 3):
            seq += 'T'
            count4 += 1
            
    return [seq, count1, count2, count3, count4]


# In[3]:


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('count', type=int)
    parser.add_argument('length', type=int)
    
    args = parser.parse_args()
    
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    outfile = open("sequences.dat", 'w')
    for i in range (args.count):
        seqInfo = generateRandomSeq(args.length)
        
        seq = seqInfo[0]
        c1 += seqInfo[1]
        c2 += seqInfo[2]
        c3 += seqInfo[3]
        c4 += seqInfo[4]
        
        outfile.write(seq + '\n')
    
    total = c1+c2+c3+c4
    p1 = c1*100/total
    p2 = c2*100/total
    p3 = c3*100/total
    p4 = c4*100/total
    
    
    
    print('\nSUMMARY\n___________________________\n')
    print('Total Nucleotides:', str(total), '\n')
    print('Observed Number of As:', str(c1), '(', str(p1), '%)')
    print('Observed Number of Cs:', str(c2), '(', str(p2), '%)')
    print('Observed Number of Gs:', str(c3), '(', str(p3), '%)')
    print('Observed Number of Ts:', str(c4), '(', str(p4), '%)\n')
        
        
        
        
    
        
    outfile.close()


# In[ ]:


main()

