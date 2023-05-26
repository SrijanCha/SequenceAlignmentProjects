#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import argparse
from matplotlib import pyplot as plt


# In[22]:


def generateMatrices(s, t, matchScore, mismatchScore, indelScore):

    # initialize arrays with s+1 rows and t+1 cols
    arrowMatrix = [['O'] * (len(t) + 1) for i in range(len(s) + 1)]
    numMatrix = [[0] * (len(t) + 1) for i in range(len(s) + 1)]

    # stop = stop
    # diag = diagonal-arrow
    # up = up-arrow
    # left = left-arrow

    # initialize corner:
    arrowMatrix[0][0] = 'stop'
    numMatrix[0][0] = 0

    # initialize first row
    for num in range(len(t)):
        i_x = num + 1
        numMatrix[0][i_x] = 0
        arrowMatrix[0][i_x] = 'stop'

    # initialize first col
    for num in range(len(s)):
        i_x = num + 1
        numMatrix[i_x][0] = 0
        arrowMatrix[i_x][0] = 'stop'

    # populate arrays
    for x in range(len(numMatrix) - 1):
        for y in range(len(numMatrix[0]) - 1):
            i_x = x + 1
            i_y = y + 1

            #find diagonal score
            match = numMatrix[x][y]
            if (s[x] == t[y]):
                match = match + matchScore
            else:
                match = match + mismatchScore

            #find up_score
            up_score = numMatrix[x][i_y] + indelScore

            #find left_score
            left_score = numMatrix[i_x][y] + indelScore

            #assign max number to the numMatrix
            numMatrix[i_x][i_y] = max(match, up_score, left_score)

            #assign arrow to arrowMatrix
            if (numMatrix[i_x][i_y] < 0):
                numMatrix[i_x][i_y] = 0
                arrowMatrix[i_x][i_y] = 'stop'
            elif (numMatrix[i_x][i_y] == match):
                arrowMatrix[i_x][i_y] = 'diag'
            elif (numMatrix[i_x][i_y] == left_score):
                arrowMatrix[i_x][i_y] = 'left'
            elif (numMatrix[i_x][i_y] == up_score):
                arrowMatrix[i_x][i_y] = 'up'
            else:
                print("oh shit") # to the grader: This will stay.
                
    
    backtrack_values = [numMatrix, arrowMatrix]
    return backtrack_values


# In[23]:


# THIS CODE WAS BORROWED FROM DISCUSSION 2 COLAB.RESEARCH NOTEBOOK - EDIT DISTANCE ALIGNMENT

def reconstruct_edit_dist(s,t, backtrack_values):

    #initialize optimal alignment strings of s and t,  s' and t', respectively
    s_align, t_align = '',''
    
    numMatrix = backtrack_values[0]
    arrowMatrix = backtrack_values[1]
    
    maxVal = 0;
    i = 0
    j = 0
    
    
    for y in range (len(numMatrix)):
        for x in range (len(numMatrix[0])):
            if(numMatrix[y][x] > maxVal):
                maxVal = numMatrix[y][x]
                i = y
                j = x

    # up, left, or diag
    while i*j!=0:
        arrow = arrowMatrix[i][j]
        if arrow == 'diag':
            s_align = s[i-1]+s_align
            t_align = t[j-1]+t_align
            i-=1
            j-=1
    
        elif arrow == 'up':
            s_align = s[i-1]+s_align
            t_align = '-'+t_align
            i-=1
    
        elif arrow =='left':
            s_align = '-'+s_align
            t_align = t[j-1]+t_align
            j-=1

        elif arrow == 'stop':
            break

        else:
            print("oh potato")

    return (s_align, t_align)


# In[24]:


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
            
    return seq


# In[36]:


def main():
    
    
    x = []
    y = []
    for i in range(19):
        alignmentLengths = []
        for j in range(100):
            s = generateRandomSeq(50*(i+1))
            t = generateRandomSeq(50*(i+1))
            (str1, str2) = (str1, str2) = reconstruct_edit_dist(s,t, generateMatrices(s, t, 1, -30, 0))
            alignmentLengths.append(len(str1))
            print(i)
        expectedAlignment = np.average(alignmentLengths)
        x.append(50*(i+1))
        y.append(expectedAlignment)
        
        
    plt.plot(x, y)


# In[39]:


main()


# In[ ]:




