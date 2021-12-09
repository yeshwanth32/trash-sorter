import socket
import os
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(26)
camera = PiCamera()

import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

def stop():
    print("stop")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    x='z'

def forward():
    print("forward")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

def backward():
    print("backward")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)

def run():
    print("run")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    #forward()

def exit():
    GPIO.cleanup()
    print("GPIO Clean up")

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
            print("motion detected...camera warming up")
            pir.wait_for_motion()
            sleep(3)
            camera.capture('camera_image.jpg')
            print("captured image....")
            print("transmitting image....")
            img = open('camera_image.jpg', 'rb')
            b_img = img.read()
            imgsize = len(b_img)
            print("sending image size")
            print(str(imgsize))
            # self.c.sendall(bytes(str(imgsize), "utf-8"))
            print("sending image")
            # self.c.sendall(b_img)
            # img.close()
            # # with open("camera_image.jpg",'rb') as file:
            # #     data = file.read(1024)
            # #     while data:
            # #         self.s.send(data)
            # #         data = file.read(1024)
            sleep(5)
            print("received response")
            recycling = True
            if (recycling):
                forward()
                sleep(6)
                stop()
                exit()
            else:
                backward()
                sleep(6)
                stop()
                exit()
            # self.s.shutdown(socket.SHUT_RDWR)
            # self.s.close()
            # self.reconnect()
                
client = Client()
