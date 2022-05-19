# -*- coding: utf-8 -*-
"""
Created on Fri May 20 08:18:26 2022

@author: Admin
"""

i = 0
a = []
tmp = 0
number_guesses = int(input("How many guesses do you want: "))


for i in number_guesses:
    tmp = input("Give me a number: ")
    a.append(tmp)
    print(a)

# =============================================================================
# while i < number_guesses:
#     i = i + 1 
#     tmp = input("Give me a number: ")
#     a.append(tmp)
#     print(a)
# =============================================================================



# =============================================================================
# a = int(input("What is a number: "))
# 
# b = int(input("Give me a second number: "))
# 
# c = input("What do you want to do?\n\r Multiply is '*' \r\n Divide is '\\'\r\n Addition is '+'\r\n Subtract is '-'\r\n ")
# 
# ## I want to get 2 numbers and then do a math thing with them
# 
# if c == '*':
#     print(a, "multiplies by ", b, "is", a*b)
# elif c == '\\':
#     print(a, "divided by ", b, "is", a/b)
#     ## Check to see if the number can be divided without a remainder
#     if ((a/b)%2) == 0:
#         print("You have a perfect division")
#     else:
#         print("You have a remainder of ", a//b)
# elif c == '+':
#     print(a, "plus ", b, "is", a+b)
# elif c == '+':
#     print(a, "plus ", b, "is", a+b)
# else:
#     print("You didn't choose a correct factor")
# 
# =============================================================================



    
