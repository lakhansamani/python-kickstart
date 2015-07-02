#Defining functions in python
import random
import sys
import os

def addNum(x,y):
    return x+y

print("enter 1st no")
x= int(sys.stdin.readline())
print("enter 2nd no")
y= int(sys.stdin.readline())

print(addNum(x,y))
