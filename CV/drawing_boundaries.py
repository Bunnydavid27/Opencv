import cv2
import numpy


img = cv2.imread('dotts.png', 0)
ret, thres_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
cnts = cv2.findContours(thres_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
cv2.drawContours(img, cnts,-1,(0,0,255),3)
s1=265
s2=267 
dots = []
contour_area = []
for cnt in cnts:
    area_cnt = cv2.contourArea(cnt)
    if s1<area_cnt<s2:
        dots.append(cnt)
        contour_area.append(area_cnt)

cv2.imshow("The Image",img )
print("Total Boundaries", len(cnts))
print("Dots", len(dots))
print('array of one dot', dots[1])
print('contour area of the dot', contour_area[1])
print("lowest contour area", min(contour_area))
print("Highest contour area", max(contour_area))
cv2.waitKey(0)
cv2.destroyAllWindows()