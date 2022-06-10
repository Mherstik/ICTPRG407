# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 08:22:29 2022

@author: Marcus
"""

inputFile = open("salary.csv", "r")

outputFile = open("newSalary.csv", "w")

def updateSalary():
    for line in inputFile:
        ## Trim the new lines
        line2 = line.rstrip("\n")
        
        ## split the line into fields
        name,num2,empid = line2.split(",")
        
        ## Check for salary
        if num2.isdigit() == False:
            outputFile.write(line)
        else: 
            ## add 5%
            num2 = float(num2) * 1.05
            outputFile.write(name + "," + str(int(num2)) + "," + empid +"\n")

updateSalary()

inputFile.close()
outputFile.close()

# =============================================================================
# ### Write to a file
# 
# fileName = input("What is the file name to create: ")
# 
# # open the file FOR WRITING!
# outputFile = open(fileName, "w")
# outputFile.write("This is NOT the first line\n")
# outputFile.write("This is the second line" + str(23) + "\n")
# outputFile.write("Line3\n")
# 
# ### Close the file
# 
# outputFile.close()
# 
# =============================================================================

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
