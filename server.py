import socket
import threading
import os

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()
    
    def accept_connections(self):
        #ip = socket.gethostbyname(socket.gethostname())
        ip = "192.168.114.208"
        port = int(input('Enter desired port --> '))

        self.s.bind((ip,port))
        self.s.listen(100)

        print('Running on IP: '+ip)
        print('Running on port: '+str(port))
        self.main()

       
    def main(self):
        c, addr = self.s.accept()
        print(c, ":", addr)

        while 1:

        # listen for ultrasonic distance sensor call
        # once that's done take a picture
        # transfer picture to client
            input("Press Enter to continue...")
            file = open("cup.jpg",'rb')
            data = file.read(1024)
            while data:
                c.send(data)
                data = file.read(1024)

            c.shutdown(socket.SHUT_RDWR)
            c.close()
            
            #threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def handle_client(self,c,addr):
        data = c.recv(1024).decode()
    
        if not os.path.exists(data):
            c.send("file-doesn't-exist".encode())

        else:
            c.send("file-exists".encode())
            print('Sending',data)
            if data != '':
                file = open(data,'rb')
                data = file.read(1024)
                while data:
                    c.send(data)
                    data = file.read(1024)

                c.shutdown(socket.SHUT_RDWR)
                c.close()
                

server = Server()
