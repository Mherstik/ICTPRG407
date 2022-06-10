# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 09:28:46 2022

@author: Marcus
"""

import random

## Generate random numbers
i = 0
# fileName = "randomnum.txt"
fileName = input("What to call it: ")
names = ["Tom","Jane","Liz", "Peter", "Mary", "Bob"]
# lines = int(input("How many lines: "))

## open for writing: 
outputFile = open(fileName, "w")

## get 10 random numbers into the file
# while i < 5:
outputFile.write("Name,Salary,Dept\n")
for n1 in names:
    r1 = random.randint(0,50)
    r2 = random.randint(20000,50000)
    r3 = random.randint(0,10)
    outputFile.write(str(n1) + "," + str(r2) + "," + str(r3) +"\n")
    i = i + 1

## close the file
outputFile.close()


