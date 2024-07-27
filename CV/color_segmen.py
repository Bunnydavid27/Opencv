import cv2
import numpy as np


def setValues(x):
    print("")


cv2.namedWindow("Color detection")
cv2.createTrackbar("Upper Hue", "Color detection",153, 180, setValues)
cv2.createTrackbar("Upper Saturation", "Color detection",255, 255, setValues)
cv2.createTrackbar("Upper Value", "Color detection",255, 255, setValues)
cv2.createTrackbar("Lower Hue", "Color detection",64, 180, setValues)
cv2.createTrackbar("Lower Saturation", "Color detection", 72, 255, setValues)
cv2.createTrackbar("Lower Value", "Color detection", 49, 255, setValues)


def get_frame(cap, scaling_factor):
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx= scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return frame

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.9
    while True:
        frame = get_frame(cap, scaling_factor)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        u_hue = cv2.getTrackbarPos("Upper Hue", "Color detection")
        u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detection")
        u_value = cv2.getTrackbarPos("Upper Value", "Color detection")
        l_hue = cv2.getTrackbarPos("Lower Hue", "Color detection")
        l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detection")
        l_value = cv2.getTrackbarPos("Lower Value", "Color detection")


        Upper_hsv = np.array([u_hue, u_saturation, u_value])
        Lower_hsv = np.array([l_hue, l_saturation, l_value])
        
        mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)

        res = cv2.bitwise_and(frame, frame, mask=mask)
        res = cv2.medianBlur(res, 5)
        cv2.imshow('Original_image', frame)
        cv2.imshow("Color_ Detector", res)
        c = cv2.waitKey(5)
        if c== 27:
            break
    cv2.destroyAllWindows()