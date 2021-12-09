
from npsocket import SocketNumpyArray
from PIL import Image
import PIL
import numpy as np
#import cv2

# cap = cv2.VideoCapture(0)
sock_sender = SocketNumpyArray()

sock_sender.initialize_sender('172.20.10.6', 7245)


image = PIL.Image.open("camera_image.jpg")
image_array = np.array(image)
sock_sender.send_numpy_array(image_array)
response = sock_sender.receive_array()
print(response)

# while True:
    
#     ret, frame = cap.read()
#     frame = cv2.resize(frame, (620, 480))
    
