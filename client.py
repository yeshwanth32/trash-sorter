import socket
import os


class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = input('Enter ip --> ')
        self.target_port = input('Enter port --> ')

        self.s.connect((self.target_ip,int(self.target_port)))
        print("connected...")

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))

    def main(self):
        while 1:
            # listen for ultrasonic distance sensor call
            # once that's done take a picture
            # transfer picture to client
            input("Press Enter to continue...")
            file = open("cup.jpg",'rb')
            data = file.read(1024)
            while data:
                self.s.send(data)
                data = file.read(1024)
            
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            self.reconnect()
                
client = Client()
