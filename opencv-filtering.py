# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 22:13:48 2018

@author: guest11
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    lower_yellow = np.array([20,100,100])
    upper_yellow = np.array([30,255,255])
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()