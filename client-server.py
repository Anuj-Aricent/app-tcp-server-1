import socket               # Import socket module
import thread

server = socket.socket()
host_server = "0.0.0.0"
port_server = 12341
server.bind((host_server, port_server))

client = socket.socket()
host_client = "127.0.0.1"
port_client = 12345
client.connect((host_client, port_client))

client_list = []

recvmsg = ""

def recvMsg(s):
    global recvmsg
    while True:
        recvmsg = s.recv(1024)
        if recvmsg:
            print  '<Recieved from main server>>> ' + recvmsg
            for c in client_list:
                c.send(recvmsg)
        
thread.start_new_thread(recvMsg, (client, ))

server.listen(5)
while True:
   c, addr = server.accept()
   if c not in client_list:
       client_list.append(c)
   buf= c.recv(1024)
   print buf
   client.send("from aseem:" + buf)
   
   continue
   c.close()
