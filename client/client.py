import socket
import sys
from this import d
from PIL import Image
import os
import io
from array import array
import base64

host='192.168.0.2'
port=50000
addr=(host,port)

pr=['1.height','2.width']

def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        try:
            s.connect(addr)
        except Exception as e:
            print('서버 (%s:%s)에 연결 할 수 없습니다.'%addr)
            sys.exit()
        print('서버 (%s:%s)에 연결 되었습니다.'%addr)
        
        fd=open('test.bmp',"rb")
        b=bytearray(fd.read())
        s.sendall(b)
        print('바이트 이미지 전송 완료')
        fd.close()
        
        for i in pr:
            msg=input(i+ ' : ')
            s.sendall(msg.encode())
            print('서버로 보냄')
        s.close()
if __name__=='__main__':
    run()