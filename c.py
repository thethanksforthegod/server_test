# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:07:44 2021

@author: Administrator
"""

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = '3.68.71.83'                          

port = 80

# connection to hostname on the port.
s.connect((host, port))                               
print('done')
# Receive no more than 1024 bytes
tm = s.recv(1024)                                     

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))