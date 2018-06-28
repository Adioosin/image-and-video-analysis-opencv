# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:59:19 2018

@author: guest11
"""

import cv2
import numpy as np

cap = cv2.VideoCapture('people-walking.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    
    fgmask = fgbg.apply(frame)
    
    cv2.imshow('orignal', frame)
    cv2.imshow('fg', fgmask)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
