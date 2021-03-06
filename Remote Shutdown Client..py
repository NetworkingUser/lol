import socket
import os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host= "192.168.2.108"
port=5050

s.connect((host,port))
    
