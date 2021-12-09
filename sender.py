
from npsocket import SocketNumpyArray
#import cv2

#cap = cv2.VideoCapture(0)
sock_sender = SocketNumpyArray()

sock_sender.initialize_sender('192.168.114.166', 9999)
image = PIL.Image.open("cup.jpg")
image_array = np.array(image)
sock_sender.send_numpy_array(image_array)

# while True:
    
#     ret, frame = cap.read()
#     frame = cv2.resize(frame, (620, 480))
    
