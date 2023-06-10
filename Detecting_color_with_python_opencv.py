"""
Detecting colored object using camera access and video processing using OpenCV,Python libraries
"""

import cv2
from Util import get_limits
from PIL import Image

vid=cv2.VideoCapture(0)
#yellow_BGR=[0,255,255] #yellow color pixel values in BGR color space
pink_BGR=[204,0,204] #pink color pixel values in BGR color space
while True:
    ret,frame=vid.read()
    hsv_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # converting rgb color space to hsv color space of frames captured from webcam/video
    ll,ul=get_limits(pink_BGR)
    mask=cv2.inRange(hsv_image,ll,ul) # Creates masks for yellow colored object identified from frame/image and 61,120 are lower and upper limits in HSV color space
    mask_pil_image=Image.fromarray(mask)
    bbox=mask_pil_image.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
        bbox_rectangle=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),10)

    # print(bbox) whenever yellow colored object identified in frame bbox co-ordinates printed

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
