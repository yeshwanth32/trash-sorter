import socket
import os
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(26)
class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = "192.168.114.166"
        self.target_port = "7425"
        #self.target_ip = input('Enter ip --> ')
        #self.target_port = input('Enter port --> ')

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
            #input("Press Enter to continue...")
            print("Waiting for no motion")
            pir.wait_for_no_motion()
            print("Waiting for motion")
            pir.wait_for_motion()
            sleep(5)
            camera.capture('camera_image.jpg')
            print("captured image....")
            print("transmitting image....")
            with open("camera_image.png",'rb') as file:
                data = file.read(1024)
                while data:
                    self.s.send(data)
                    data = file.read(1024)
            
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            self.reconnect()
                
client = Client()
