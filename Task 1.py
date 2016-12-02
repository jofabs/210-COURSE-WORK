""" Task 1
Write a function that randomly shuffles an array of integers
and explain the rationale behind its implementation."""

import random

Num = [0,13,3,5,6,98]

def randomRearrange(Num):
    newList=[]
    while Num != []:
        i=random.choice((Num))
        newList.append(i)
        Num.remove(i)
        print(i,Num,newList)
    return newList

print ("Original range of numbers are", Num)
print("this is the new result", randomRearrange(Num))


# ATTEMPT 1 Random.shuffle solution EASY STEP
#theNum = ['0','13','3','5','6','98']
#random.shuffle(theNum)
#print (theNum)
