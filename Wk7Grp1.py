# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 08:22:29 2022

@author: Marcus
"""

## Get file name

fileName = input("What file do you want: ")
# file2 = ""

# Open the file
fileInput = open(fileName, "r")
# file2Input = open(filename,"r")

### Read lines from file
for line in fileInput:
    print(line, end='')
    
## Close the file
fileInput.close()
