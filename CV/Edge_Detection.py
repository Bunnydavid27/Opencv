import cv2
import numpy as np

image = cv2.imread('Images\maria.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gradients_sobelx = cv2.Sobel(image, -1, 1, 0)
gradients_sobely = cv2.Sobel(image, -1, 0, 1)
gradients_sobelxy = cv2.Sobel(image, -1, 1, 1)
gradients_sobelxy_add = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)
gradients_laplacian = cv2.Laplacian(image, -1)
canny = cv2.Canny(image, 80, 150)



cv2.imshow('image', image)
cv2.imshow('gradients_sobelx', gradients_sobelx)
cv2.imshow('gradients_sobely', gradients_sobely)
cv2.imshow('gradients_sobelxy', gradients_sobelxy)
cv2.imshow('gradients_sobelxy_add', gradients_sobelxy_add)
cv2.imshow('gradients_laplacian', gradients_laplacian)
cv2.imshow('canny', canny)

cv2.waitKey(0)






