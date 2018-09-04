import numpy as np 

from PIL import ImageGrab 
import cv2
import time
from directkeys import ReleaseKey, PressKey,W,A,S,D


last_time = time.time()

while(True):
    printscreen_pil = ImageGrab.grab(bbox=(0,40,1000,800))
    printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8')
    print('loop took {} seconds '.format(time.time()-last_time))
    
    last_time = time.time()
    cv2.imshow('window',np.array(printscreen_pil))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    