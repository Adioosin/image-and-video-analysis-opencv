# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:35:01 2018

@author: guest11
"""

import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,255,255), 15)
cv2.rectangle(img, (15,25), (200,150), (0,255,0),5)
cv2.circle(img, (100,63),55,(0,0,255),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10],[100,90]], np.int32)
cv2.polylines(img,[pts], True, (0,255,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX

#cv2.putText(image,text,start coordinate,font,size,color_text,thickness,anti-aliasing)
cv2.putText(img, 'OpenCV Dude!', (0,130), font, 2, (200,255,255), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()