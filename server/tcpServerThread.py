import socket, threading
from PIL import Image
import os
import io


class TCPServerThread(threading.Thread):
    def __init__(self, tcpServerThreads, connections, connection, clientAddress):
        threading.Thread.__init__(self)
        
        self.tcpServerThreads=tcpServerThreads
        self.connections=connections
        self.connection=connection
        self.clientAddress=clientAddress
        
    def run(self):
        try:
            length=self.connection.recv(4)
            int_length=int.from_bytes(length,byteorder='big')
            print(int_length)
            byte_image=self.connection.recv(int_length)
            #print(byte_image)
            if int_length ==0:
                return
            data_io=io.BytesIO(byte_image)
            image=Image.open(data_io)
            image.save('image/test.jpg')
                
        except Exception as e:
            print(e)
            
        subThread=TCPServerThread(self.tcpServerThreads,self.connections,self.connection,self.clientAddress)
        subThread.start()
