import numpy as np
import cv2

img = np.zeros((500,500))
cv2.imwrite("Output/zeros_img.jpg", img)

img[ : , : ] = 100

cv2.imwrite("Output/100_img.jpg", img)

img = img+10
cv2.imwrite("Output/100+10_img.jpg", img)

#value = 110

img[ 100:200 , 100:200 ] = 255
cv2.imwrite("Output/box_img.jpg", img)
