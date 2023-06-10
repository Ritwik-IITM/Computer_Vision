import numpy as np
import cv2

def get_limits(color):
    c=np.uint8([[color]]) # Inserting the BGR values which we want to convert into HSV
    hsvc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    ll=hsvc[0][0][0]-10,100,100
    ul=hsvc[0][0][0]+10,255,255
    ll=np.array(ll,dtype=np.uint8)
    ul=np.array(ul,dtype=np.uint8)
    return ll,ul
