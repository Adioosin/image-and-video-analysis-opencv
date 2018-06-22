# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:02:17 2018

@author: guest11
"""

import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

roi = img[100:150, 100:150]
img[0:50, 0:50] = roi

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindow()