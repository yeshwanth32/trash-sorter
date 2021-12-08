import socket
import threading
import os

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()
    
    def accept_connections(self):
        ip = socket.gethostbyname(socket.gethostname())
        #ip = "192.168.114.208"
        port = int(input('Enter desired port --> '))

        self.s.bind((ip,port))
        self.s.listen(100)

        print('Running on IP: '+ip)
        print('Running on port: '+str(port))
        while 1:
            c, addr = self.s.accept()
            print(c, " ,", addr)
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()

       
    # def main(self):
    #     c, addr = self.s.accept()
    #     print(c, ":", addr)

    #     while 1:

    #     # listen for ultrasonic distance sensor call
    #     # once that's done take a picture
    #     # transfer picture to client
    #         input("Press Enter to continue...")
    #         file = open("cup.jpg",'rb')
    #         data = file.read(1024)
    #         while data:
    #             c.send(data)
    #             data = file.read(1024)

    #         c.shutdown(socket.SHUT_RDWR)
    #         c.close()
            
    #         #threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def handle_client(self,c,addr):
        file_name = "temp"
        write_name = 'from_server '+file_name
        if os.path.exists(write_name): os.remove(write_name)

        with open(write_name,'wb') as file:
            while 1:
                data = c.recv(1024)
                if not data:
                    break
                file.write(data)

        print(file_name,'successfully downloaded.')
        c.shutdown(socket.SHUT_RDWR)
        c.close()
                

server = Server()
