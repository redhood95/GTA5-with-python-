import numpy as np 

import pyscreenshot as ImageGrab
import cv2
import time

last_time = time.time()
while(True):
    printscreen = ImageGrab.grab()#specify the location of the game window using bbox
    im2 = np.asanyarray(printscreen)
    #printscreen_numpy = np.array(printscreen.getdata(),dtype = 'uint8').reshape((printscreen.size,printscreen.size[0],3))
    cv2.imshow('window',im2)
    print