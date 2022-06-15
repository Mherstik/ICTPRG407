# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:06:12 2022

@author: Marcus
"""

import os

netoctet = input("Give me the first 3 octects: ")
nethost = input("Give me the last octect: ")

print("The host to ping is "+netoctet+"."+nethost)

net = netoctet+"."+nethost
response = os.system("ping -n 1 "+ net)

## for linux
# response = os.system("ping -c 1 "+ net)

if response == 0:
    print("Ping to ", net, "show it's up")
if response != 0:
    print("Ping to ", net, "didn't work")
    
'''
get IP
get port

loop connecting to each SCOKET (a socket is an IP address : a port) 
        use connect_ex
        
if it connects say it's up!!
if not - say it's down

3.3
read from the port? get 1024 bytes??

'''