# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:01:28 2022

@author: Marcus
"""


fruit = ["banana", "apple", "strawberry", 'grape', 'pinapple', 'blueberry', "raspberry"]
search = input("What do you want to search for: ")
print("You are looking for:", search)
if search in fruit:
    print("True")
else:
    print("False")



#### Part 1


# # ## NO NO # Take an input sentence
# # Ask for a letter and search for it in the sentence
# # Where is it?
# position = 0

# sentence = "The quick brown fox jumps over the lazy dog"
# search = input("Give me a letter to search for: ")
# if search in sentence:
#     print("The letter", search, "is in there")
# ## where is it??
# for letter in sentence:
#     position = position + 1
#     if search == letter:
#         print(search + " is in position: ", position)






# ## remember the range!!
# for x in range(6): 
#     print(x)


### SLICING!!

# s = "Monty Python"

# # M o n t y   P y t h o  n
# # 0 1 2 3 4 5 6 7 8 9 10 11

# print(s[4])
# print(s[0:4]) # position 0 to 4 not including position 4
# print("Jump from 6 to 4 with 1 space each", s[6:4:-1]) # from 6 to 4, jump in minus 1

# print(s[2:9:2])
# print(s[:4])
# print(s[4:])

###


# myStr = "Dennis Rodman"
# # print(len(myStr))
# # print(myStr[4])
# # for letter in myStr:
# #     print(letter)

# ## count the number of "n" in myStr

# count = 0
# for letter in myStr:
#     if letter.lower() == 'd':
#         count = count + 1
# print(count)


# names = ["Tom Jones", "Barry White", "Urtha Kitt"]
# # print(len(names))
# i = 0
# for name in names:
#     for letter in name:
#         #print(i, letter)
#         #if i == 12:
#         #if letter == "t" or letter == "T":
#         if letter.upper() == "T":
#             #print("Letter",i, "is", letter)
#             i = i +1
# print(i)


        
    #print("\r####")
    

# singer = "Tom Jones"
# length = len(singer)
# # print(length)
# #print(singer[4])

# #print(singer[9])
# i = 0
# while i < len(singer):
#     print(i, singer[i])
#     i = i + 1

# print("######")

# # for letter in singer:
# #     print(letter)
# for t in singer:
#     print(t)




# #singer[4] = 'p'
# #### Lists

# names = ["Tom Jones", "Barry White", "Urtha Kitt", 3.6, 4]
# print(len(names))
# print(names[2])

# names[2] = 'p'
# print(names[2])
# print(type(names))
# for name in names:
#     print (name)



# height = input("What is your height: ")
# height = float(height)
# print("You are " + str(height) + "m tall") 



# a = 1
# b = 12.7
# c = "Tom"

# d = str(23.9)
# e = str(30)

# print("A is a", type(a))
# print("B is a", type(b))
# print("C is a", type(c))

# print(a + b)
# print(b * 5) # float * 5
# print(c * 5) # string * 5

# print(str(b) + c)

# print("a + b = " + (str(a) + str(b)))

# print(int(b))
# print(float(a))

# print(b//2)
# print(b%2)
# print(len(c))


# print(int(float(d)))
# print(int(e))
