import numpy as np
import cv2
import math
# from textDetection import textDetection
from matplotlib import pyplot as plt

def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def find_closest_points(points):
    num_points = len(points)
    closest_points = [None] * num_points
    for i in range(num_points):
        min_distance = float('inf')
        for j in range(num_points):
            if i != j:
                distance = euclidean_distance(points[i], points[j])
                if distance < min_distance:
                    min_distance = distance
                    closest_points[i] = points[j]
    return closest_points

def plot_distribution(data_array):
    plt.hist(data_array, bins=10, edgecolor='black')  # You can adjust the number of bins as per your preference
    plt.xlabel('Values')
    plt.ylabel('Frequency') 
    plt.xticks([np.min(data_array),np.mean(data_array),np.max(data_array)])

img_path='test_img/front/Phosp-5hr-front-05.tif'
img = cv2.imread(img_path, 0)
content_img = img[0:512, 0:512]
text_img = img[513:550,257:423]
# text=textDetection(text_img)
scale=cv2.threshold(text_img, 100, 255, cv2.THRESH_BINARY)[1]
pixels=np.argwhere(scale == 255)
max_x = 1
min_x = 0
for pixel in pixels:
    if pixel[0]>max_x:
        max_x=pixel[1]
    if pixel[0]<min_x:
        min_x=pixel[1]
scale_bar=max_x-min_x
kernel = np.ones((3,3), np.uint8)
content_blur = cv2.GaussianBlur(content_img, (3,3), 0)
# edges = cv2.Canny(content_blur,24,200)
ret, edges=cv2.threshold(content_blur,100,255,cv2.THRESH_BINARY_INV)
close = cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel,iterations=3)
result = cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel,iterations=3)
cnts = cv2.findContours(result, cv2.RETR_LIST,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
for cnt in cnts:
    cv2.drawContours(result,[cnt], 0, (255,255,255), -1)

minArea = 10
xcnts = []
xcnts_area = []
xcnts_distance = []
for cnt in cnts:
    if minArea<len(cnt):
        x, y = cnt.mean(axis=0)[0]
        xcnts.append([x,y])
        xcnts_area.append(len(cnt))
        print(len(cnt))
xcnts_closest_points=find_closest_points(xcnts)
for i in range(len(xcnts)):
    xcnts_distance.append(euclidean_distance(xcnts[i],xcnts_closest_points[i]))
plt.figure('result')
plt.subplot(231),plt.imshow(content_img,cmap = 'gray')
plt.title('Original Image (%s)'%(img_path)), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(result,cmap = 'gray')
plt.title('Holes'), plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(text_img,cmap = 'gray')
plt.text(0,50,'Scale bar length is %s pixels'%(scale_bar),style='italic',color='red', fontsize=8)
plt.title('Scale'), plt.xticks([]), plt.yticks([])
plt.subplot(234),plot_distribution(xcnts_area)
plt.title('Area')
plt.subplot(235),plot_distribution(xcnts_distance)
plt.title('Distance')
plt.show()