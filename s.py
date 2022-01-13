import socket                                         

serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = ''                          

port = 5556                                           

# bind to the port
serversocket.bind((host, port))                                  
serversocket.listen(1) 

print('waitiiiing')
f=open("s.txt","w")
f.write("no")
f.close()
while True:
    clientsocket,addr = serversocket.accept()      
    f=open("s.txt","w")
    f.write(addr[0])
    f.close()
    s='connected'
    clientsocket.send(s.encode('ascii'))
    clientsocket.close()
    break
