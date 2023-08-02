import numpy as np
import cv2
from matplotlib import pyplot as plt

class MyImage:
    def __init__(self, img_name):
        self.img = cv2.imread(img_name)
        self.__name = img_name

    def __str__(self):
        return self.__name
img = cv2.imread('test_img/back/Phosp-1hr-back-04.tif', 0)
img_name=MyImage(img)
print(str(img_name))