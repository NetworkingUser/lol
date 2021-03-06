import socket
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=5050

s.bind((host,port))
s.listen(1)

con,addr=s.accept()
os.system("start")
