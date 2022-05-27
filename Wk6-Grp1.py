#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 10:46:51 2022

@author: Marcus Hersik

Description: Count the number of steps to find a number using bisectional sort

Licence: GPL v2

"""

lowPage=1
highPage=100000
midPage=0
target=650
numLoops=0
#Stop this search when we're within two pages of our target
while ((highPage - lowPage) > 2):
        print("Now checking from page " + str(lowPage) + " to page " + str(highPage))
        #midPage = ((lowPage + highPage) // 2) #find the middle of this section
        midPage = ((lowPage + highPage) / 2) #find the middle of this section
        midPage = int(midPage)
        if midPage < target:
            lowPage = midPage +1 #our guess was too low, update our lower bound
        elif midPage > target:
            highPage = midPage -1 #our guess was too high, update our upper bound
        else:
            print("We found the exact page")
        numLoops = numLoops + 1
        
print("We finished between page " + str(lowPage) + " and page " + str(highPage))
print("We found the right page after " + str(numLoops) + " attempts.")