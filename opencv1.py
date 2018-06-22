# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:10:38 2018

@author: Aditya
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg',1)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0
# =============================================================================
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()