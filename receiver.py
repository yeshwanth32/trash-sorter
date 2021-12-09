
import cv2
from npsocket import SocketNumpyArray
from PIL import Image
from obj_test import *


while True:
    sock_receiver = SocketNumpyArray()
    sock_receiver.initalize_receiver(7245)

    frame = sock_receiver.receive_array()  # Receiving the image as numpy array. 
    pil_image=Image.fromarray(frame)
    pil_image.save("received_image.jpg")
    detect_picture("received_image.jpg")
