# -*- coding: utf-8 -*-
"""
Created on Fri May  6 08:21:21 2022

@author: Marcus Herstik
"""


## Calculate wages

import random

hourlyWage = random.randrange(35, 50)
#print(hourlyWage)

#test = random.choice(["cybersecurity","W10","potato","Smelly marcus","python"])
#print(test)

# get hours worked
hoursWorked = float(input("How many hours did you work this week: "))

# gross = hours worked * hourly wage
# hourlyWage = float(input("What is your hourly rate: "))
gross = hoursWorked * hourlyWage


# if commissions new gross = gross + comission
commission = input("Did you get a commission? Y or N: ")
if commission == "Yes" or commission == "Y" or commission == "y":
    commRate = float(input("What is the commission amount in $$: "))
    gross = gross + commRate

# remove tax @ 15% 
net = gross - (gross *.15)

# remove super @10% + salary sac = $50 p/m, studnet loan = $100p/m etc = net
net = net - (net *.1) - (50/4) - (100/4)
# put net in bank account
print("You will receive: $" + str(net))




# =============================================================================
# ### Pseudocode Example
# Repeat until no swapping was done {
#     For each position in the list from lowest up to (not including) highest {
#             If the element at this position is bigger than the next position {
#                 Swap this element and the next element
#                 Record that a swap was done
#                 }
#             }
#     }
# # preswap
# [21, 15, 99, 77, 45, 56]
# 
# ## 1st swap
# 
# [15, 22, 99, 77, 45, 56]
# 
# ## 2nd swap
# [15, 22, 77, 99, 45, 56]
# 
# ## 3rd swap
# [15, 22, 77, 45, 99, 56]
# 
# ## 4th
# [15, 22, 77, 45, 56, 99 ]
# 
# ## 5
# [15, 22, 45, 77, 56, 99 ]
# 
# ## 6
# [15, 22, 45, 56, 77, 99 ]
# 
# =============================================================================


## Part 1 post break


# =============================================================================
# # a = int(input("Enter 1st integer: "))
# # b = int(input("Enter 2nd integer: "))
# # c = int(input("Enter 3rd integer: "))
# # d = float(input("Enter 4th decimal: "))
# 
# # print("Convert d to integer", int(d))
# # print(a+b+c)
# # print(a+int(d))
# 
# # e = float(input("Enter 5th decimal: "))
# # f = float(input("Enter 6th decimal: "))
# # print(d*e/f)
# 
# # r = float(input("Radius: "))
# # print("Radius: ", r, "Diameter: ", r*2, "Area: ", 3.14159*r**2)
# # print("#####\r\n OPTION 2\r\n ####")
# # print("Radius: %.1f Diameter: %.1f Area: %.5f" %(r,r*2, 3.14159*r**2))
# =============================================================================



### BREAK 

# =============================================================================
# age = int(input("What is your age: "))
# print("Your age is", age)
# print("Your age is " + str(age))
# 
# 
# if age >= 13:
#     #print("Age is 13 or over")
#     if age <= 19:
#         print("You are a teenager")
#     #elif age >19:
#     else:
#         print("You are too old")
# else:
#     print("Age is less than 13")
#     
# 
# if age >= 13 and age <= 19:
#     print("1 line- you are a teenager")
# else: 
#     print("You are the wrong age")
# 
# print("You have reached the end")
# =============================================================================

### Part 3

# =============================================================================
# mark = int(input("What did you score: "))
# 
# if (mark < 50):
#     print("Fail")
# elif mark < 65:
#     print("Pass")
# elif mark < 75:
#     print("Credit")
# elif mark < 85:
#     print("Distinction")
# else:
#     print("HD")
# =============================================================================

### Part 2

# =============================================================================
# age = int(input("what is your age: "))
# 
# if age != 18:
#     print("You receive a 20% discount")
#     print("Ice-cream is delicious")
# print("Please follow the waiter")
# =============================================================================

### Part 1

# =============================================================================
# # name = "Tom"
# name = input("What is your name? ")
# 
# ### Marcus will teach conditional statements
# if name != "Marcus":
#     print("Yay")
#     print("I'm not a fan of Marcus")
#     print("He is smelly!!")
# else:
#     print("Boo!!")
#     
# number = 2+2
# print(number)   
# 
# decimal = 4.0+2.0
# print(decimal)
# 
# print(decimal + number)
# 
# print(type(name))
# print(type(number))
# print(type(decimal))
# =============================================================================
