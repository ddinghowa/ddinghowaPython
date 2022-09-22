import socket, threading
import sys
from PIL import Image
from array import array
from random import uniform
import struct
import time

host='172.30.1.41'
port=50001
addr=(host,port)

    
def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        try:
            s.connect(addr)
        except Exception as e:
            print('서버 (%s:%s)에 연결 할 수 없습니다.'%addr)
            sys.exit()
        print('서버 (%s:%s)에 연결 되었습니다.'%addr)
        
        
        while True: 
            posx=uniform(-0.001,0.001)
            posy=uniform(-0.001,0.001)
            posz=uniform(-0.001,0.001)
            rotx=uniform(-0.001,0.001)
            roty=uniform(-0.001,0.001)
            rotz=uniform(-0.001,0.001)
            bax=bytearray(struct.pack("f",posx))
            bay=bytearray(struct.pack("f",posy))
            baz=bytearray(struct.pack("f",posz))
            bax2=bytearray(struct.pack("f",rotx))
            bay2=bytearray(struct.pack("f",roty))
            baz2=bytearray(struct.pack("f",rotz))
            s.sendall(bax)
            s.sendall(bay)
            s.sendall(baz)
            s.sendall(bax2)
            s.sendall(bay2)
            s.sendall(baz2)
            time.sleep(0.1)
        
        
if __name__=='__main__':
    run()
