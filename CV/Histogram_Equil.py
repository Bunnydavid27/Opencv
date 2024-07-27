import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Images\low_contrast_img.jpg')


img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([img], [0], None,  [256], [0,255])
cv2.imshow('img', img)
plt.plot(hist)

#Equalizing Histograms and intensities spreading in bins uniformly
equal_hist_image = cv2.equalizeHist(img)
hist2 = cv2.calcHist([equal_hist_image], [0], None,  [256], [0,255])
cv2.imshow('Equalized', equal_hist_image)
plt.plot(hist2)


plt.show()
cv2.waitKey(0)
