# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 08:22:29 2022

@author: Marcus
"""

### Write to a file

fileName = input("What is the file name to create: ")

# open the file FOR WRITING!
outputFile = open(fileName, "w")
outputFile.write("This is NOT the first line\n")
outputFile.write("This is the second line" + str(23) + "\n")
outputFile.write("Line3\n")

### Close the file

outputFile.close()


# =============================================================================
# ### Read a file
# 
# ## Get file name
# # fileName = input("What file do you want: ")
# fileName = "Wk7Text.txt"
# # file2 = ""
# 
# # Open the file
# fileInput = open(fileName, "r")
# # file2Input = open(filename,"r")
# 
# ### Read lines from file
# for line in fileInput:
#     print(line, end='')
#     
# ## Close the file
# fileInput.close()
# =============================================================================
