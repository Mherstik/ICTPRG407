# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:01:26 2022

@author: Marcus Herstik
"""

numbers = []
i = 1

a = 'string'
print(a)

b = int(input("How many numbers do you want to give: "))
print("We will loop "+ str(b)+ " number of times")

## get a list of numbers
## loop b amount of times getting numbers in a list
while i < b:
    i = i + 2
    tmp = input("Give me a number: ")
    numbers.append(tmp)
    print("i is" + str(i),"\r\n","tmp is"+ str(tmp),"\r\n","numbers is"+ str(numbers))