# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:01:26 2022

@author: Marcus Herstik
"""

numbers = []
i = 1

#a = 'string'
#print(a)

b = int(input("How many numbers do you want to give: "))
a = int(input("give me another number: "))
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
 

factor = input("What do you want to do? \r\n Multiply is '*' \r\n Divide is '\\' \r\n Addition is '+' \r\n Subtract is '-'\r\n \r\n : " )

# get the numbers and then do factor

if factor == '*':
    print(a, "multiplied by ", b , "is", a*b)
elif factor == '\\':
    print(a, "divided by ", b , "is", a/b)
    ## Check to see if the number can be divided without a remainder
    
elif factor == '+':
    print(a, "plus", b , "is", a+b)
elif factor == '-':
    print(a, "minus", b , "is", a-b)
else:
    print("You didn't choose a correct factor!")
    
    
    
    
    