from http import client
import socket, threading
import tcpServerThread

class TCPServer(threading.Thread):
    def __init__(self,HOST,PORT):
        threading.Thread.__init__(self)
        
        self.HOST=HOST
        self.PORT=PORT
        
        self.serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.HOST, self.PORT))
        self.serverSocket.listen(1)
        
        self.connections=[]
        self.tcpServerThreads=[]
        
    def run(self):
        try:
            while True:
                print('tcp server :: server wait...')
                connection, clientAddress=self.serverSocket.accept()
                self.connections.append(connection)
                print("tcp server :: connect : ",clientAddress)
                
                subThread=tcpServerThread.TCPServerThread(self.tcpServerThreads,self.connections,connection,clientAddress)
                subThread.start()
                self.tcpServerThread.append(subThread)
        except:
            print("tcp server :: serverThread error")
    