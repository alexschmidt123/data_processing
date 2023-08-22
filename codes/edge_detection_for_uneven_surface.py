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

def get_longest_distance(data_array):
    max_x=1
    min_x=520
    max_y=1
    min_y=520
    for data in data_array:
        if data[1]>max_x: 
            max_x=data[1]
        if data[1]<min_x:
            min_x=data[1]
        if data[0]>max_y: 
            max_y=data[0]
        if data[0]<min_y:
            min_y=data[0]
    longest_x=max_x-min_x
    longest_y=max_y-min_y
    return [longest_x,longest_y]

def exact(data_array):
    pairs=[]
    for array in data_array:
        pairs.append([array[0][0],array[0][1]])
    return(pairs)

img_path='test_img/front/Phosp-5hr-front-05.tif'
img = cv2.imread(img_path, 0)
content_img = img[0:512, 0:512]
text_img = img[513:550,257:423]
# text=textDetection(text_img)
scale=cv2.threshold(text_img, 100, 255, cv2.THRESH_BINARY)[1]
pixels=np.argwhere(scale == 255)
scale_bar=get_longest_distance(pixels)
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

minArea = 5
xcnts = []
xcnts_area = []
xcnts_distance = []
for cnt in cnts:
    cnt_t=exact(cnt)
    print(cnt_t)
    cnt_t_size=get_longest_distance(cnt_t)
    print(cnt_t_size)
    avg_diameter=0.5*(cnt_t_size[0]+cnt_t_size[1])
    if minArea<avg_diameter:
        x, y = cnt.mean(axis=0)[0]
        xcnts.append([x,y])
        xcnts_area.append(avg_diameter)
xcnts_closest_points=find_closest_points(xcnts)
for i in range(len(xcnts)):
    xcnts_distance.append(euclidean_distance(xcnts[i],xcnts_closest_points[i]))
plt.figure('result')
plt.subplot(231),plt.imshow(content_img,cmap = 'gray')
plt.title('Original Image (%s)'%(img_path)), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(result,cmap = 'gray')
plt.title('Holes'), plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(text_img,cmap = 'gray')
plt.text(0,50,'Scale bar length is %s pixels'%(scale_bar[0]),style='italic',color='red', fontsize=8)
plt.title('Scale'), plt.xticks([]), plt.yticks([])
plt.subplot(234),plot_distribution(xcnts_area)
plt.title('Diameter(pixel)')
plt.subplot(235),plot_distribution(xcnts_distance)
plt.title('Distance(pixel)')
plt.show()