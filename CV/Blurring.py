import cv2
import numpy as np


img = cv2.imread('Images\maria.jpg')


#kernel_blurr

kernel = np.ones((25, 25), dtype=np.float32) / 625.0
output_kernel_blur = cv2.filter2D(img, -1, kernel)

#Boxfilter Blurr

output_blur = cv2.blur(img, (25, 25))
output_box = cv2.boxFilter(img, -1, (5, 5), normalize=False) #True for normalizing the matrix


#Gaussian Blurr
Gaussian_blurr = cv2.GaussianBlur(img, (5,5), 0)

#Median Blurr REduction NOise
Median_Blurr = cv2.medianBlur(img, 5)


#Bilateral(Reducing Noise and Preseving edges)
Bilateral_blurr = cv2.bilateralFilter(img, 5, 6, 6)


cv2.imshow("Kernel_blurr", output_kernel_blur)
cv2.imshow("Output Blurr fun", output_blur)
cv2.imshow("Boxfilter Blurr", output_box)
cv2.imshow("Gaussian Blurr", Gaussian_blurr)
cv2.imshow("Bilateral_blurr", Bilateral_blurr)
cv2.imshow("Original", img)
cv2.waitKey(0)



