import socket
import threading

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Start Messaging")
def receiver():
  ip = "192.168.1.11"
  port = 1234
  s.bind((ip,port))
  while True:
    x = s.recvfrom(1024)
    data = x[0].decode()
    print("\t\t\t\t"+data)
    
    #client_ip = x[1][0]
    #client_port = x [1][1]
    


def sender():
  while True:    
    msg = input("")
    msg = bytes(msg,'utf-8')
    client_ip = "192.168.1.12"
    client_port= 2345
    s.sendto( msg, (client_ip, client_port) )

#create thread

x1 = threading.Thread(target=sender)

x2 = threading.Thread(target=receiver)

# start a thread
x1.start()

x2.start()

