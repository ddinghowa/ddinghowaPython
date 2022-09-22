import socket
import sys
import struct
import time

host = '172.30.1.41'
port = 50001
addr = (host, port)

    
def tcp_send(info):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        try:
            s.connect(addr)
        except Exception as e:
            print('서버 (%s:%s)에 연결 할 수 없습니다.'%addr)
            sys.exit()
        print('서버 (%s:%s)에 연결 되었습니다.'%addr)        
        
        # info_bytearray = bytearray(struct.pack("i", info + i))
        # s.sendall(info_bytearray)

        # test code

        while True:
            info_bytearray = bytearray(struct.pack("i", info))

            s.sendall(info_bytearray)

            time.sleep(1)

            print(info)

            info = (info % 3) + 1
            
        
if __name__=='__main__':
    tcp_send(-1)
