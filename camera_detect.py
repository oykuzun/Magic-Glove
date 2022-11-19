from picamera2 import Picamera2
from time import sleep

# if button pressed called this function

def image_capture(path):

    camera = Picamera2()
    sleep(2)
    camera.start()
    camera.capture_file("/home/magicglove/MagicGlove/test/image.jpg")
    sleep(2)

if __name__ == "__main__":
    image_capture("test")
