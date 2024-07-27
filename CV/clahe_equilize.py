import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Images\maria.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=2)
clahe_img = clahe.apply(gray)

normal_equal = cv2.equalizeHist(gray)

cv2.imshow('Normal', gray)
cv2.imshow('normal_equal',normal_equal)
cv2.imshow('clahe_img', clahe_img)

cv2.waitKey(0)

