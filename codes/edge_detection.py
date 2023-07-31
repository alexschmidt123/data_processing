import numpy as np
import cv2
import math
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

img = cv2.imread('test_img/front/Phosp-1hr-front-02.tif', 0)
content_img = img[0:512, 0:512]
text_img = img[513:572,0:512]
kernel = np.ones((3,3), np.uint8)
content_blur = cv2.GaussianBlur(content_img, (3,3), 0)
img_binary = cv2.threshold(content_blur, 155, 255, cv2.THRESH_BINARY)[1]
edges = cv2.Canny(img_binary,100,200)
dilate = cv2.dilate(edges,kernel,iterations=1)

cnts = cv2.findContours(dilate, cv2.RETR_LIST,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
# filter by area
for cnt in cnts:
    cv2.drawContours(dilate,[cnt], 0, (255,255,255), -1)

minArea = 10
xcnts = []
xcnts_area = []
xcnts_distance = []
for cnt in cnts:
    if minArea<cv2.contourArea(cnt):
        x, y = cnt.mean(axis=0)[0]
        xcnts.append([x,y])
        xcnts_area.append(cv2.contourArea(cnt))
    else:
        cv2.drawContours(dilate,[cnt], 0, (0,0,0), -1)
xcnts_closest_points=find_closest_points(xcnts)
for i in range(len(xcnts)):
    xcnts_distance.append(euclidean_distance(xcnts[i],xcnts_closest_points[i]))
plt.figure('result')
plt.subplot(221),plt.imshow(content_img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(dilate,cmap = 'gray')
plt.title('Holes'), plt.xticks([]), plt.yticks([])
plt.subplot(223),
plot_distribution(xcnts_area)
plt.title('Area')
plt.subplot(224),plot_distribution(xcnts_distance)
plt.title('Distance')
plt.show()