import cv2
import numpy as np

# Read the image
img = cv2.imread('Images/shps.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and help contour detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Use Canny edge detector to find edges
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the edges image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through each contour
for contour in contours:
    # Approximate the contour to reduce the number of vertices
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Get the number of vertices
    vertices = len(approx)

    # Determine the shape based on the number of vertices
    if vertices == 3:
        shape = 'Triangle'
    elif vertices == 4:
        if cv2.contourArea(contour) > 500:
            shape = 'Rectangle' 
        else:
            shape = 'Square'
    elif vertices == 5:
        shape = 'Pentagon'
    else:
        shape = 'Circle'

    # Draw the shape name on the image
    cv2.putText(img, shape, (approx[0][0][0], approx[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

# Display the result
cv2.imshow('Shape Recognition', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
