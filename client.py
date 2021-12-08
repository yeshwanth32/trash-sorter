import socket
import os
from obj_test import *

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = input('Enter ip --> ')
        self.target_port = input('Enter port --> ')

        self.s.connect((self.target_ip,int(self.target_port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))

    def main(self):
        while 1:
            file_name = "temp"
            write_name = 'from_server '+file_name
            if os.path.exists(write_name): os.remove(write_name)

            with open(write_name,'wb') as file:
                while 1:
                    data = self.s.recv(1024)

                    if not data:
                        break

                    file.write(data)

            print(file_name,'successfully downloaded.')
            output = detect_picture("from_servertemp")
            print(output)
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            self.reconnect()
                
client = Client()
