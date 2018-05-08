import numpy as np 

import pyscreenshot as ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey,W,A,S,D



    



def process_img(image):
    process_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    process_img = cv2.Canny(process_img,threshold1=200,threshold2=300)
    return process_img


for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

last_time = time.time()
while(True):
    printscreen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))#specify the location of the game window using bbox
    #im2 = np.asanyarray(printscreen)
    new_screen = process_img(printscreen) 
    
    #printscreen_numpy = np.array(printscreen.getdata(),dtype = 'uint8').reshape((printscreen.size,printscreen.size[0],3))
    print('down')
    Presskey(W)
    time.sleep(3)
    print('up')
    PressKey(W)
    print('loop took {} seconds'.format(time.time()-last_time))
    last_time=time.time()
    cv2.imshow('window',new_screen)
   # cv2.imshow('window',cv2.cvtColor(np.array(printscreen),cv2.COLOR_BGR2RGB))
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


