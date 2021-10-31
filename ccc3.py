import socket
import  random

random.seed(1)

filename   = "9.pdf"
 

serverAddressPort   = ("41.35.38.228", 10001)

bufferSize          = 2020

s = 0
with open(filename, "wb") as f:
    while  True:
        port=random.randrange(1500,39999)
        try:
            UDPClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            UDPClient.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            UDPClient.settimeout(0.5)
            UDPClient.bind(("",0))
            UDPClient.sendto(b"0", serverAddressPort)
            bytes_read = UDPClient.recvfrom(bufferSize)
            s=s+len(bytes_read[0])
            if b"01010101010101010101" in bytes_read[0]:
                f.close()
                break
            f.write(bytes_read[0])
            b=0
        except:
            print(10001)
            pass
        print(s)
