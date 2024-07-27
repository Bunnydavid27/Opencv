import cv2
import numpy as np

def setValues(x):
    print("")

cap = cv2.VideoCapture(0)
cv2.namedWindow("Color detection")
cv2.createTrackbar("Upper Hue", "Color detection",153, 180, setValues)
cv2.createTrackbar("Upper Saturation", "Color detection",255, 255, setValues)
cv2.createTrackbar("Upper Value", "Color detection",255, 255, setValues)
cv2.createTrackbar("Lower Hue", "Color detection",64, 180, setValues)
cv2.createTrackbar("Lower Saturation", "Color detection", 72, 255, setValues)
cv2.createTrackbar("Lower Value", "Color detection", 49, 255, setValues)




while(True):
    cv2.waitKey(1000)
    ret, init_frame = cap.read()
    if(ret):
        break



    
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    u_hue = cv2.getTrackbarPos("Upper Hue", "Color detection")
    u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detection")
    u_value = cv2.getTrackbarPos("Upper Value", "Color detection")
    l_hue = cv2.getTrackbarPos("Lower Hue", "Color detection")
    l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detection")
    l_value = cv2.getTrackbarPos("Lower Value", "Color detection")

    kernel = np.ones((3,3), np.uint8)

    Upper_hsv = np.array([u_hue, u_saturation, u_value])
    Lower_hsv = np.array([l_hue, l_saturation, l_value])
    
    mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
    mask = cv2.medianBlur(mask, 3)
    mask_inv = 255 - mask
    mask = cv2.dilate(mask, kernel, 5)

    b = frame[:,:,0]
    g = frame[:,:,1]
    r = frame[:,:,2]
    b = cv2.bitwise_and(mask_inv, b)
    g = cv2.bitwise_and(mask_inv, g)
    r = cv2.bitwise_and(mask_inv, r)
    frame_inv = cv2.merge([b,g,r])

    b = init_frame[:,:,0]
    g = init_frame[:,:,1]
    r = init_frame[:,:,2]
    b = cv2.bitwise_and(b, mask)
    g = cv2.bitwise_and(g, mask)
    r = cv2.bitwise_and(r, mask)
    blanket_area = cv2.merge([b,g,r])


    final = cv2.bitwise_or(frame_inv, blanket_area)

    cv2.imshow('Original_image', frame)
    cv2.imshow("Potter Cloak", final)
    c = cv2.waitKey(5)
    if c== 27:
        break
cv2.destroyAllWindows()