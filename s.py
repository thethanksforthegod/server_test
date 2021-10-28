# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:07:51 2021

@author: Administrator
"""

import socket                                         
import time

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = ''                          

port = 5556                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           
print('waitiiiing')
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    s='hhhhhhhhhhhhhhhhhhhhhhhhhhh'
    clientsocket.send(s.encode('ascii'))
    clientsocket.close()