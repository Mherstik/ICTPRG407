# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:01:26 2022

@author: Marcus Herstik
"""

i = 1
a = 10

## only go to a max of 5
while int(a) > 5:
    a = int(input("How many loops do you want: "))
    print("You must choose a number no higher than 5")

servers = ['A', 'B', "C", 'D', "E"]

for server in servers:
    while i < a:
        i = i + 1
        print("Server "+server)
        ## print only that amount
    

#a = 'string'
#print(a)
# numbers = []
# i = 1
# a = int(input("How many numbers do you want to give: "))
# b = int(input("give me another number: "))
#print("We will loop "+ str(b)+ " number of times")

## get a list of numbers
## loop b amount of times getting numbers in a list
# while i <= b:
#     tmp = input("Give me a number: ")
#     numbers.append(tmp)
#     # print("i is " + str(i))
#     # print("tmp is "+ str(tmp))
#     # print("numbers is "+ str(numbers))
#     i = i + 1
 

# =============================================================================
# factor = input("What do you want to do? \r\n Multiply is '*' \r\n Divide is '\\' \r\n Addition is '+' \r\n Subtract is '-'\r\n \r\n : " )
# 
# # get the numbers and then do factor
# 
# if factor == '*':
#     print(a, "multiplied by ", b , "is", a*b)
# elif factor == '\\':
#     print(a, "divided by ", b , "is", a/b)
#     ## Check to see if the number can be divided without a remainder
#     if ((a/b)%2) == 0:
#         print("You have perfect division")
#     else:
#         print("You have a remainder of", a%b)
# elif factor == '+':
#     print(a, "plus", b , "is", a+b)
# elif factor == '-':
#     print(a, "minus", b , "is", a-b)
# else:
#     print("You didn't choose a correct factor!")
# =============================================================================
    
    
    
    
    