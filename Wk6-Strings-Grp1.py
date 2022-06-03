# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 08:27:52 2022

@author: Marcus
"""



secondString = "piano"

while True:
    firstString = input("Enter some text: ")
    if firstString == secondString:
        print(firstString, "is equal to", secondString)
    elif firstString < secondString:
        print(firstString, "comes before", secondString)
    elif firstString > secondString:
        print(firstString, "comes after", secondString)
    else:
        print("Never get here!")


# x = range(1,7,2)
# for n in x:
#     print(n)


# ## check for names in list

# names = ["Tom Jones", "Barry White", "Urtha Kitt"]

# check = "t"

# for name in names:
#     # print(name, names)
#     if check.upper() in name.upper():
#         print("True")
#     else:
#         print("False")


# # slicing 

# s = "Monty Python"

# #print(s)
# ask = input("What to search for: ")
# if ask in s:
#     print("True")
# else:
#     print("False")


# print(len(s))
# print(s[4])
# print(s[:4]) # get upto the 4th index, exclusive

# print(s[4:7])   # from 4 upto 7, excluding 7
# print(s[:5])    # up to 5, not including 5
# print(s[6:])    # from 6 to the end

# print(s[6:7])


# ## count the number of letters

# word = "banana"
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1

# print(count)

# names = ["Tom Jones", "Barry White", "Urtha Kitt"]
# count2 = 0
# ## count the number of letter T's
# for name in names:
#     for letter in name:
#         if letter.lower() == 't': # converts string 
#         # if letter.lower == "t": ## doesn't convert string
# #        if letter == 't' or letter == "T": # checks both
#             count2 = count2 + 1
# print(count2)

# name = "Benny Hill"
# # length = len(name)
# # print(type)
# print(name + " is length of " + str(len(name)))

# # name[4] = 'p'

# # print(name[15])

# i = 0
# while i < len(name):
#     #print("Letter number " + str(i) + " is " + name[i])    
#     print(i, name[i])
#    # print(i)
#     i = i +1

# for letter in name:
#     print(letter)
    
# names = ["Tom Jones", "Barry White", "Urtha Kitt"]
# for singer in names:
#     #print(singer)
#     for letter in singer:
#         print(letter)

# =============================================================================
# ### Convert sting numbers to int and float
# 
# price = 3.2
# print(price)
# dollars = int(price)
# print(dollars)
# 
# num1 = 1.5
# print(int(num1))
# 
# num2 = str(2.1)
# print(int(float(num2)))
# 
# 
# #num3 = int(input("Input: "))
# num3 = str(3)       # works
# print(int(num3))
# 
# num4 = str(4.0)
# print(int(num4))    # doesn't work
# =============================================================================



# =============================================================================
# a = 1
# b = 1.0
# c = "Tom"
# d = ["a","b", 1.0, 4]
# 
# user = input("Give me a number: ")
# print("The user gave me a", type(user))
# user = float(user)
# user = user//1
# print("User is", user, type(user))
# print("I have changed it to an integer =", int(user))
# 
# 
# # answer = 4 * float(user)
# # print("4 times", user,"is", answer)
# # answer = 4 * user
# # print("4 times", user,"is", answer)
# # print("A is a", type(a))
# # print("B is a", type(b))
# # print("C is a", type(c))
# # print("D is a", type(d))
# 
# 
# =============================================================================
