import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.GaussianBlur(img, (11,11), 0)
    conv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("Original", img)
    cv2.imshow("HSV", conv)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.waitKey(0)