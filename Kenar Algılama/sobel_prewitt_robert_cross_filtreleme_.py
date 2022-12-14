# -*- coding: utf-8 -*-
"""Sobel - Prewitt - Robert cross filtreleme .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13W2HcrAF_EpVz-O_uSNt5ySIW4bUD5Ks
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Resmi yükleme
img = cv2.imread('apple.jpeg') 
cv2_imshow(img)

 
# Grayscale'e çevirme işlemi
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Daha iyi bir sonuç için Blur ekleniyor
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
# Sobel Kenar Algılama
print("Sobel Kenar Algılama")
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) 
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) 
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) 
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
cv2_imshow(np.hstack((sobelx,sobely,sobelxy,edges)))

#Prewitt kenar Algılama
print("Prewitt Kenar Algılama")
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_blur, -1, kernelx)
img_prewitty = cv2.filter2D(img_blur, -1, kernely)
cv2_imshow(np.hstack((img_prewittx,img_prewitty)))

#Robert-Cross kenar Algılama
print("Robert-Cross kenar Algılama")
roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
  
roberts_cross_h = np.array( [[ 0, 1 ],
                             [ -1, 0 ]] )
  
img = cv2.imread("apple.jpeg",0).astype('float64')
img/=255.0
vertical = ndimage.convolve( img, roberts_cross_v )
horizontal = ndimage.convolve( img, roberts_cross_h )
  
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
edged_img*=255
cv2.imwrite("output.jpg",edged_img)
cv2_imshow(edged_img)