# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:05:11 2018

@author: Aditya
"""

import cv2
import numpy as np

img =cv2.imread('threshold.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 1)
gaus2 = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 1)

retval2, otsu = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# =============================================================================
# cv2.imshow('orignal',img)
# cv2.imshow('threshold',threshold)
# cv2.imshow('grayscale',threshold2)
# =============================================================================
cv2.imshow('gaus',gaus)
cv2.imshow('gaus2',gaus2)
# =============================================================================
# cv2.imshow('otsu',otsu)
# =============================================================================

cv2.waitKey(0)
cv2.destroyAllWindows()