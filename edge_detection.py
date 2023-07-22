import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('test_img/hole1.tif', 0)
content_img = img[0:512, 0:512]
text_img = img[513:572,0:512]

edges = cv.Canny(content_img,125,200)
BnW_image = cv.adaptiveThreshold(content_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv.THRESH_BINARY,11,2)
plt.subplot(131),plt.imshow(content_img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(edges,cmap = 'gray')
plt.title('Edges'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(BnW_image,cmap = 'gray')
plt.title('BW'), plt.xticks([]), plt.yticks([])
plt.show()