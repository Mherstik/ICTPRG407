# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:13:28 2022

@author: Marcus
"""


nameList = []
numList = []

name = "dummy name"
number = 0

while name != '':
    name = input("Enter a name: ")
    # nameList.append(name)
    # if name.isdigit():
    #     print("No numbers!")
    #     name = input("Enter a name: ")
    if name != '':
        while number != 0:
            number = input("Give me a number: ")
            if number.isdigit():
                numList.append(number)
                nameList.append(name)





# for num1 in range(1,6):
#     print("This is the first for loop")
#     for num2 in range(1,6):
#         print("This is the second for loop")
#         print("The total of", num1, "plus", num2, "is", num1+num2)
        
###
## 1,1 -> 1,2 - > 1,3 -> 1,4
## 1,1 -> 2,1 -> 3, 1 -> 4,1


# =============================================================================
# ## Only give me numbers!!
# 
# numList = []
# number = 0
# 
# ## keep adding numbers until they press enter
# 
# while number != '':
#     number = input("Give me a number: ")
#     ## Test is it a number
#     if number.isdigit() == True:
#         ## add to the number list?
#         numList.append(int(number))
#     else:
#         print("Give me a number!!")
#         number = input("Give me a number: ")
# 
# print("Finished giving numbers")
# =============================================================================

  

### Get list of names until they they enter a blank name

# nameList = []
# name = "dummy name"

# while name != '':
#     name = input("Enter a name: ")
#     # nameList.append(name)
#     # if name.isdigit():
#     #     print("No numbers!")
#     #     name = input("Enter a name: ")
#     if name != '':
#         nameList.append(name)

    

# =============================================================================
# 
# ### LISTS
# 
# nameList = []
# 
# nameList.append("Marcus")
# nameList.append("Andrew")
# nameList.append("Sharon")
# #print(nameList[3])
# 
# # for each in nameList:
# #     print(each)
#     
# print(len(nameList))
# i = 0
# 
# while i < len(nameList):
#     print(nameList[i])
#     i+=1
# =============================================================================


## Example 2 - FOR loop

# for num in range(0,5):
#     print(num)

# for num in range(0,5,5):
#    print(num)

# for num in range(0,30,5):  # (starting, stopping exclusive, stepping)
#     print(num)
    
# # Ex3 iterate over a list!
# dayName = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ]
# for day in dayName:
#     print("We are open " + str(day))

# # index = int(input("What day number do you want?\r\n"
# #                   "1=Monday,2=Tues,3=Wed,4=Thurs...\r\n: "))
                  
# # print(dayName[index -1])

# # print(len("Marcus"))
# print(len(dayName))

# =============================================================================
# # keep looping
# keepLooping = "y"
# userInput = "y"
# 
# while keepLooping =="y":
#     print("Hello there")
#     userInput = input("Do you want to loop? ")
#     
# print("Finished looping forever!!!")
# 
# =============================================================================

# =============================================================================
# # Careful of infinite loops!!
# 
# i = 1
# while i > 0:
#     print(i)
#     i+=1
#     if i > 1000:
#         break
# 
# print('You broke out!!')
# =============================================================================


# =============================================================================
# # Ex1 - While loop
# num1 = 0
# total = 0
# userInput = "y" ## this sets the first condition
# 
# while userInput.lower() =="y":
#     num1 = int(input("Enter a number: "))
#     total = total + num1
#     userInput = input("Continue y/n ")
# print("The total was: " + str(total))
# 
# ## which line above ensures the INITIAL condition is true!!
# =============================================================================

################

# Intro



## This is a variable
# a = 1
# b = "Tom"

# print(str(a) + b)

# myName = input("What is your name? ")

# print(myName) 
# print('myName')

# age = input("What is your age? ")
# print("My age is " + age)

# ageNextYear = int(input("Your age? ")) + 1
# print(ageNextYear)

## Test how old a person is.
# When age is over 45 - say "Ok Boomer"
# When age is under 45 - say "Young blood... 
# Exactly 45 - say not long now!!

# age = int(input("How old are you? "))

# if age > 45:
#     print("Ok Boomer")
# elif age < 45:
#     print("Young blood...")
# else:
#     print("Not long now")

