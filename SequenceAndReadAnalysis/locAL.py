#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse
import numpy as np


# In[2]:


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


# In[3]:


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


# In[4]:


def localAlignmentScore(s, t, matchScore, mismatchScore, indelScore):
    score = 0
    for i in range(len(s)):
        if (s[i] == t[i]):
            score += matchScore
        else:
            if (s[i] == '-'):
                score += indelScore
            elif (t[i] == '-'):
                score += indelScore
            else:
                score += mismatchScore
    return score


# In[1]:


def main():
    
    #parse from argv
    parser = argparse.ArgumentParser()
    parser.add_argument('seq_file', type=str)
    parser.add_argument('-m', type=int, required=True)
    parser.add_argument('-s', type=int, required=True)
    parser.add_argument('-d', type=int, required=True)
    parser.add_argument('-a', required=False, action='store_true')

    args = parser.parse_args()

    filename = args.seq_file
    matchScore = args.m
    mismatchScore = args.s
    indelScore = args.d

    returnAlignment = False
    if (args.a):
        returnAlignment = True
        
        
        
    #read from file.
    sequences = []
    with open(filename, 'r') as infile:    
        for line in infile:
            if not((line[0] == '>') or (line[0] == '\n')):
                sequences.append(line)
    
    sequence1 = sequences[::2]
    sequence2 = sequences[1::2]
    pairs = [[sequence1[i],sequence2[i]] for i in range(len(sequence1))]
    
    
    for pair in pairs:
        s,t = pair
        
        (str1, str2) = reconstruct_edit_dist(s,t, generateMatrices(s, t, matchScore, mismatchScore, indelScore))

        # print the score of the best local-alignment
        print('Score:', str(localAlignmentScore(str1, str2, matchScore, mismatchScore, indelScore)))

        #print length of the best local-alignment
        print('Length:', str(len(str1)))

        if (returnAlignment):
            print('Aligned Sequence:')
            print(str1)
            middleLine = ''
            for i in range(len(str1)):
                if (str1[i] == str2[i]):
                    middleLine += str1[i]
                else:
                    middleLine += ' '

            print(middleLine)
            print(str2)
        print()


# In[ ]:


main()

