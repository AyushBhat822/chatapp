import socket
import threading
import time

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

def connect_server():
    time.sleep(15)
    server_ip = "ip_addr"
    server_port = port_no_server
    while True:
        msg = input("")
        msg = bytes(msg, 'utf-8')
        s.sendto(msg,(server_ip, server_port))
        time.sleep(30)

def acting_as_server():
    server_ip = "ip"
    server_port = port_no
    s.bind((server_ip, server_port))
    while True:
        x = s.recvfrom(1024)
        data = x[0].decode()
        print("\t\t\t\t"+ data)

x1 = threading.Thread(target=connect_server)
x2 = threading.Thread(target=acting_as_server)

x2.start()
x1.start()

