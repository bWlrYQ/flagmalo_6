import socket
from threading import *
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

message = "Give flag pl3@se :"

server_address = ('0.0.0.0', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

with open("./flag.txt") as f:
            flag = f.read()
            print(flag)

class client(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.start()

    def compare(self, user_input):
        if len(user_input) == 0 or len(user_input) > len(flag):
            print("bad length")
            return False
    
        if user_input.lower() == "stop":
            print("stopped")
            exit(1)
    
        for i in range(len(user_input)):
            print("trying " + user_input[i] + " vs " + flag[i])
            if user_input[i] != flag[i]:
                return False
            sleep(0.25)
        return True

    def run(self):
        print('connection from', self.addr)
        while True:
            self.conn.sendall(message.encode())
            indata = self.conn.recv(4096)
            if indata:
                print('received {!r}'.format(indata.decode()))
                print('answering client')
                self.compare(indata.decode())

        self.conn.close()


sock.listen(20)
print('server started and listening')
while True:
    conn, addr = sock.accept()
    client(conn, addr)