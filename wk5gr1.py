# -*- coding: utf-8 -*-
"""
Created on Fri May 20 08:18:26 2022

@author: Admin
"""

### Debug this file
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        



# ## count to 4
# for count in range(1,4):
#     print(count)

# =============================================================================
# import pandas as pd
# 
# df = pd.read_csv("test.com")
# 
# bill = 67
# n = int(input("Number of people: "))
# 
# share = bill/n
# print("Share of the bill is", share)
# =============================================================================



# =============================================================================
# i = 0
# a = []
# tmp = 0
# number_guesses = int(input("How many guesses do you want: "))
# 
# servers = ['A', 'B', 'C', 'D']
# 
# 
# for server in servers:
#     print("Server"+server)
# 
# for server in servers:
#     while i < number_guesses:
#         i = i + 1
#         print("Server"+server+" is item number", i)
#         break
# =============================================================================


# =============================================================================
# 
# for i in number_guesses:
#     tmp = input("Give me a number: ")
#     a.append(tmp)
#     print(a)
# =============================================================================

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



    
