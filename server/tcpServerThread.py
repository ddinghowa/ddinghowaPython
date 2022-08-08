import socket, threading
from PIL import Image
import os
import io

pr=['height','width','']

class TCPServerThread(threading.Thread):
    def __init__(self, tcpServerThreads, connections, connection, clientAddress):
        threading.Thread.__init__(self)
        
        self.tcpServerThreads=tcpServerThreads
        self.connections=connections
        self.connection=connection
        self.clientAddress=clientAddress
        
    def run(self):
        try:
            byte_image= self.connection.recv(65536) #아마 바이트크기
            print('tcp server(client) :: bytes image : ',byte_image)
            
            for i in pr:
                if(i==""):
                    
                    print("전송 완료. 바이트 이미지 복원하시겠습니까?(y/n)")
                    ans=input(':')
                    
                    if(ans=='y'):
                        image=Image.open(io.BytesIO(byte_image))
                        image.show()
                    print('tcp server(client) :: exit!!')
                    print('tcp server :: server wait')
                    break
                data =self.connection.recv(1024)
                #int.from_bytes(data, byteorder='big')
                print('tcp server(client) -', i, end=" ")
                print(':', data.decode())
                
                try:
                    int_data=int(data.decode())
                    print('int형:', int_data)
                except:
                    print('int형 변환 불가')
                    pass
            
        except:
            self.connections.remove(self.connection)
            self.tcpServerThreads.remove(self)
            exit(0)
        self.connections.remove(self.connection)
        self.tcpServerThreads.remove(self)
        
    def send(self, message):
        print('tcp server :: ',message)
        try:
            for i in range(len(self.connections)):
                self.connections[i].sendall(message.encode())
        except:
            pass