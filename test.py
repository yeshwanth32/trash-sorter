from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/camera_image.jpg')
camera.stop_preview()
