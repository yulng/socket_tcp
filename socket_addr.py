# -*- coding: utf-8 -*-
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('0.0.0.0', 5000))


time.sleep(4)
sock.send('1')
print(sock.recv(1024))
sock.close()
