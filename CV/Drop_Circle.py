import cv2
import numpy as np


#Canvas
canvas = np.zeros((512, 512,3), dtype=np.uint8)


#Mouse Event Function
def drawCircle(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(canvas, (x, y), 10, (0, 255, 0), 3)


cv2.namedWindow('image')
cv2.setMouseCallback('image', drawCircle)


while(1):
    cv2.imshow('image', canvas)
    if cv2.waitKey(20) == ord('q'):
        break

cv2.destroyAllWindows()