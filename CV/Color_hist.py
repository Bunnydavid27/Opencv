import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Images\maria.jpg')
b, g, r = cv2.split(img)
cv2.imshow('Image', img)
hist_b = cv2.calcHist([b], [0], None, [256], [0, 255])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 255])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 255])
plt.plot(hist_b)
plt.plot(hist_g)
plt.plot(hist_r)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
v_equal = cv2.equalizeHist(v)
enchanced_img = cv2.merge((h, s, v_equal))
enchanced_img = cv2.cvtColor(enchanced_img, cv2.COLOR_HSV2BGR)
b2, g2, r2 = cv2.split(enchanced_img)
cv2.imshow('Enchanced Image', enchanced_img)
hist_b2 = cv2.calcHist([b2], [0], None, [256], [0, 255])
hist_g2 = cv2.calcHist([g2], [0], None, [256], [0, 255])
hist_r2= cv2.calcHist([r2], [0], None, [256], [0, 255])
plt.plot(hist_b2)
plt.plot(hist_g2)
plt.plot(hist_r2)


plt.show()
cv2.waitKey(0)