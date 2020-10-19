from time import sleep
from picamera import PiCamera
from datetime import datetime
import os

# convert h264 to mp4
# ffmpeg -framerate 25 -i Vid_0.h264 -c copy output.mp4
# or with transcode
# ffmpeg Vid_0.h264 output.mp4



# from https://picamera.readthedocs.io/en/release-1.10/api_camera.html

#camera = PiCamera(resolution=(1280, 720), framerate=30)
camera = PiCamera(resolution=(1280, 720), framerate=25)
#camera = PiCamera(resolution=(640, 480), framerate=15)
#camera.sensor_mode = 6 # V2 1280x720 binned x 2
#camera.sensor_mode = 6
#v1: 4	1296x972
#v1: 5	1296x730

#camera.sensor_mode = 5 
#camera.sensor_mode = 5

# Set ISO to the desired value
#camera.iso = 400


now = datetime.now();
print(now);

nam = 'Vid_'
nam2 = 'Vid_0.h264'

x=1
max_segments = 100
segment = 0
segment_length = 20*60; 

camera.start_preview(alpha=230,fullscreen=False, window = (30, 10, 1280, 720))

while x :

    nam2 = 'videos/' + nam + str(segment) +'.h264'
    print(nam2)
    

    camera.start_recording(nam2)
    camera.wait_recording(segment_length)
    camera.stop_recording()

    segment = segment+1
    if ( segment > max_segments ):
        segment = 0;


        
camera.stop_preview()



