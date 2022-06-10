# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:29:07 2022

@author: Marcus
"""

# begin
# open old file
inputFile = open("salaries.csv",'r')
# open a new file
outputFile = open('newSalaries.csv', "w")

# get a line
for each in inputFile:
    # trim the line end from end
    lineStrip = each.rstrip("\n")
    # split into variables 
    name, salary, dept = lineStrip.split(",")
    # check if it has a salary
    # if not 
    if salary.isdigit() == False:
        # 	print to file
        outputFile.write(each)
    elif salary.isdigit() == True:
      # if yes get salary * 1.05, put line back together & 	print to file
        if int(dept) == 2:
              salary = float(salary) * 2
              outputFile.write(name + "," + str(int(salary)) + "," + dept + "\n")
    
        else: 
              salary = float(salary) * 1.05
              outputFile.write(name + "," + str(int(salary)) + "," + dept + "\n")
    else:
        print("not,here,today")
      
# close files
inputFile.close()
outputFile.close()

# end



# import random

# ### create a CSV with 5 people
# ## salary between 30k and 50K
# #  & dept id between 1 and 10

# names = ["Tom", 'Jane', "Bob", "Mary", "Ash"]

# # get file name
# fileName = input("What do you want to call the file: ")

# # open file for writing!!
# outputFile = open(fileName,"w")

# ## write the data
# outputFile.write("Name,Salary,Dept ID`\n")

# # generate random data for each person
# for name in names:
#     s1 = random.randint(30000,50000)
#     dept = random.randint(1,10)
#     #print(name +","+ str(s1) +","+str(dept) )
#     outputFile.write(name +","+ str(s1) + "," + str(dept) + "\n")


# ## close the file
# outputFile.close()


# import pandas as pd

# data = pd.read_csv("https://raw.githubusercontent.com/Mherstik/ICTPRG407/main/iris.csv")

# print(data)

# inputFile = open("data.txt","r")

# for blah in inputFile:
#     print(blah, end='')

# inputFile.close()

# ##

# print("\nOVERWRITE THE FILE!!\n")

# # outputFile = open("data.txt","a") # append to end of find
# outputFile = open("data.txt","a") #write
# outputFile.write("\nHello, World\n")
# outputFile.write("How are you? I am" + str(23) +"\n")
# outputFile.write("I am fine\n")

# outputFile.close()