
from npsocket import SocketNumpyArray
from PIL import Image
import PIL
import numpy as np
from picamera import PiCamera
from time import sleep

#import cv2

# cap = cv2.VideoCapture(0)
sock_sender = SocketNumpyArray()
camera = PiCamera()

sock_sender.initialize_sender('192.168.201.166', 7245)
print("motion detected...camera warming up")
camera.start_preview()
sleep(3)
camera.capture('camera_image.jpg')
camera.stop_preview()
image = PIL.Image.open("camera_image.jpg")
image_array = np.array(image)
sock_sender.send_numpy_array(image_array)


# def send_file(file_name):
#     image = PIL.Image.open("camera_image.jpg")
#     image_array = np.array(image)
#     sock_sender.send_numpy_array(image_array)
    


# while True:
    
#     ret, frame = cap.read()
#     frame = cv2.resize(frame, (620, 480))
    
