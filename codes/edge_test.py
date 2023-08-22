import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

def extract(tree):
    for x in range(len(tree)):
        if type(tree[x]) == list:
            tree[x] = extract(tree[x])
        else:
            return tree[x]

    return tree

img_path='test_img/back/Phosp-1hr-back-04.tif'
img = cv2.imread(img_path, 0)
content_img = img[0:512, 0:512]




kernel = np.ones((3,3), np.uint8)
content_blur = cv2.GaussianBlur(content_img, (3,3), 0)
ret, edges=cv2.threshold(content_blur,100,255,cv2.THRESH_BINARY_INV)
close = cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel,iterations=3)
result = cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel,iterations=3)
cnts = cv2.findContours(result, cv2.RETR_LIST,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
for cnt in cnts:
    cv2.drawContours(result,[cnt], 0, (255,255,255), -1)
print(cnts[1])
pairs=[]
for array in cnts[1]:
        pairs.append([array[0][0],array[0][1]])
print(pairs)