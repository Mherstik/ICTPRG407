# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 09:28:46 2022

@author: Marcus
"""

import random

## Generate random numbers
i = 0
fileName = "randomnum.txt"
lines = int(input("How many lines: "))

## open for writing: 
outputFile = open(fileName, "w")

## get 10 random numbers into the file
while i < lines:
    r1 = random.randint(0,50)
    r2 = random.randint(0,50)
    r3 = random.randint(0,10)
    outputFile.write(str(r1) + " , " + str(r2) + " , " + str(r3) +"\n")
    i =+ 1

## close the file
outputFile.close()


