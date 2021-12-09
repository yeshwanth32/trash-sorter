import socket
import threading
import os
from obj_test import *

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()
    
    def accept_connections(self):
        ip = socket.gethostbyname(socket.gethostname())
        port = 7425
        #ip = "192.168.114.208"
        #port = int(input('Enter desired port --> '))

        self.s.bind((ip,port))
        self.s.listen(100)

        print('Running on IP: '+ip)
        print('Running on port: '+str(port))
        # try:
        #     os.remove('from_server_temp.jpg')
        # except:
        #     print("Error while deleting file ")
        while 1:
            c, addr = self.s.accept()
            print(c, " ,", addr)
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def wait_for_acknowledge(client,response):
        """
        Waiting for this response to be sent from the other party
        """
        amount_received = 0
        amount_expected = len(response)
        
        msg = str()
        while amount_received < amount_expected:
            data = client.recv(16)
            amount_received += len(data)
            msg += data.decode("utf-8")
            #print(msg)
        return msg

    def handle_client(self,c,addr):
        file_name = "_temp.png"
        write_name = 'from_server'+file_name
        # try:
        #     os.remove('from_server_temp.jpg')
        # except:
        #     print("Error while deleting file ", write_name)
        image_size = c.recv(16)
        image = c.recv(int(image_size))
        
        # with open(write_name,'wb') as file:
        #     while 1:
        #         data = c.recv(1024)
        #         if not data:
        #             break
        #         file.write(data)

        print(file_name,'successfully downloaded.')
        #output = detect_picture("from_server_temp.png")
        #print(output)
        c.shutdown(socket.SHUT_RDWR)
        c.close()
                

server = Server()
