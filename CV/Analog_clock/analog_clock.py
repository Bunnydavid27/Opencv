import cv2
import numpy as np
import math
import datetime

def draw_hand(image, angle, length, color, thickness):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    
    endpoint_x = int(center[0] + length * math.cos(math.radians(angle)))
    endpoint_y = int(center[1] + length * math.sin(math.radians(angle)))
    
    cv2.line(image, center, (endpoint_x, endpoint_y), color, thickness)

def draw_clock_face(image):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    radius = min(center) - 10
    cv2.circle(image, center, radius, (255, 255, 255), 2)

def update_clock(image):
    current_time = datetime.datetime.now().time()
    
    hour_angle = 90 - (current_time.hour % 12 + current_time.minute / 60) * 30
    minute_angle = 90 - current_time.minute * 6
    second_angle = 90 - current_time.second * 6

    draw_hand(image, hour_angle, image.shape[1] // 4, (0, 0, 255), 6)
    draw_hand(image, minute_angle, image.shape[1] // 2 - 10, (255, 255, 255), 4)
    draw_hand(image, second_angle, image.shape[1] // 2 - 10, (0, 255, 0), 2)

# Create a black canvas
canvas_size = 500
clock_face = np.zeros((canvas_size, canvas_size, 3), dtype=np.uint8)

while True:
    # Draw clock face
    draw_clock_face(clock_face)
    
    # Update clock hands based on current time
    update_clock(clock_face)

    # Display the clock
    cv2.imshow('Motion Analog Clock', clock_face)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

    # Clear the canvas for the next frame
    clock_face.fill(0)

cv2.destroyAllWindows()
