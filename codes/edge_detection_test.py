import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('test_img/front/Phosp-1hr-front-03.tif', 0)
content_img = img[0:512, 0:512]
text_img = img[513:572,0:512]
kernel = np.ones((7,7), np.uint8)
kernel1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_image = cv2.filter2D(content_img, -1, kernel1)
img_binary = cv2.threshold(sharpened_image, 180, 255, cv2.THRESH_BINARY)[1]
edges = cv2.Canny(img_binary,100,200)
dilate = cv2.dilate(edges,kernel,iterations=1)


plt.figure(1)
plt.subplot(221),plt.imshow(content_img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(sharpened_image,cmap = 'gray')
plt.title('blur'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_binary,cmap = 'gray')
plt.title('binary'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(dilate,cmap = 'gray')
plt.title('dilate'), plt.xticks([]), plt.yticks([])
plt.show()