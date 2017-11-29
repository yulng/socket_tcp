# -*- coding: utf-8 -*-
import socket
import logging
import time

logging.basicConfig(filename='socket_server.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 5000))
sock.listen(5)


while True:
    conn, addr = sock.accept()
    time.sleep(3)
    try:
        conn.settimeout(3)
        buf = conn.recv(1024)
        if buf == '1':
            conn.send('welcome to tcp socket')
            logging.info('server send a socket')
        else:
            conn.send('what the fuck')
            logging.info('what the fuck')
    except socket.timeout:
        print('socket timeout')
        logging.error('socket timeout')
    conn.close()
