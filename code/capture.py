import time
import picamera

camera = picamera.PiCamera()
camera.start_preview()
time.sleep(5)

camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

print 'Image captured...'