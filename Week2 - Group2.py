# -*- coding: utf-8 -*-
"""
Created on Fri May  6 13:00:54 2022

@author: Marcus Herstik
"""



print("This is a code area") # this is an inline comment

# THis is a comment

'''
This is the problem statement

Come up with pseudocode to calculate an employee’s pay
Consider such things as:
Gross salary is hours * hourly wage
Do they get commissions, a bonus?
How to deduct PAYG tax
Other deductions: super, salary sacrifice etc.

'''
### Marcus pseudocode

net = 0
bonusAmount = 0

# get employee hourly rate
hourlyRate = float(input("What is your hourly rate: "))

# find out how many hours worked
hoursWorked = float(input("How many hours were worked in the last fortnight: "))

# multiply hourly rate x hours worked
gross = hoursWorked * hourlyRate

# add any commissions
bonus = str(input("Did you recieve a bonus this fortnight (y/n): "))
if bonus.lower() == "yes" or bonus.lower() == "y":
    bonusAmount = float(input("How much did you earn (in $$): "))
# else: 
#     bonusAmount = 0

gross = gross + bonusAmount
print("Your gross is $"+str(gross))

# deduct any tax @15%, super @10%, salary sacrifice 100/pm, student loans 80 p/m
net = gross - (gross * .15) - (gross * .1) - (100/4) - (80/4)

taxedGross = gross * .15
deductedGross = gross * .1

net2 = gross - taxedGross - deductedGross - (100/4) - (80/4)
# provide final pay

print("You earned $"+str(net))
print("You earned NET2 $%.2f" %(net2))  # this is an inline comment


# =============================================================================
# # a = int(input("Give integer: "))
# # b = int(input("Give integer: "))
# # c = int(input("Give integer: "))
# 
# # print(a+b+c)
# 
# # d = float(input("Give me a decimal: "))
# # e = float(input("Give me a decimal: "))
# # f = float(input("Give me a decimal: "))
# # print(d*e/f)
#           
# # print(int(d))
# 
# 
# # r = float(input("Radius of circle is: "))
# # rDiameter  = r*2
# # rArea = 3.14159 * r**2
# 
# # print("Radius:", r, "Diameter:", rDiameter, "Area:", rArea )
# 
# # print("Radius: %.1f Diameter: %.1f Area: %.6f" %(r, r*2, 3.14159*r**2))
# =============================================================================

#################

#####
## 
## BREAK
##
#####

# =============================================================================
# age = int(input("what is your age? "))
# 
# if age >= 13:
#     print("You are over 13")
#     if age <=19:
#         print("You are under 19")
#         print("you are a teenager")
#     elif age >19:
#         print("you are too old")
#     else:
#         print("Never get to!!")
# else:
#     print("you are too young")
# =============================================================================
    



# =============================================================================
# ## Get mark from student and say grade
# 
# mark = int(input("What is your grade? "))
#            
# if mark < 50:
#     print("Fail")
# elif mark < 65:
#     print("Pass")
# elif mark < 75:
#     print("Credit")
# elif mark < 85:
#     print("DN")
# else:
#     print ("HD")
# =============================================================================



# =============================================================================
# name = input("What is your name? ")
# 
# if not name == "Marcus":
#     print("You are my favourite")
# else:
#     print("Go away!!")
# 
# =============================================================================

# =============================================================================
# print("Welcome to the Python Restaurant")
# name = input("What is your name? ")
# print("Nice to meet you", name)
# 
# age = int(input("what is your age? "))
# 
# if age < 18:
#     print("You get 20% off")
#     print("Try the ice-cream")
# elif age > 45 and age < 60:
#     print("Would you like a drink?")
# elif age > 60 and age < 100:
#     print("You get a 10% discount")
#     print('Do you need your food mushed up?')
# elif age == 100:
#     print("Get a letter from the Queen")
# else:
#     print('You are in between')
# print("Please follow the waiter")
# =============================================================================

# =============================================================================
# year = 2022 
# myAge = int(input("what year where you born "))
# currentAge = year - myAge
# print("I am " + str(currentAge) + " this year")
# 
# =============================================================================

# =============================================================================
# ### Revision
# a = int(input("Give me an integer: "))
# b = input("Give me your name: ")
# c = float(input("Give me a decimal: "))
# 
# print(a,b,c)
# 
# print(a + c)
# 
# print(str(a) + b + str(c))
# 
# print("a is of type", type(a))
# print("b is of type", type(b))
# print("c is of type", type(c))
# 
# print(2+2)
# =============================================================================
