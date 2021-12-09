
import cv2
from npsocket import SocketNumpyArray
from PIL import Image

sock_receiver = SocketNumpyArray()
sock_receiver.initalize_receiver(7245)


frame = sock_receiver.receive_array()  # Receiving the image as numpy array. 
pil_image=Image.fromarray(frame)
pil_image.show()
response = [1]
sock_receiver.send_numpy_array(response)