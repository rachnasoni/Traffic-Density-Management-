import cv2
import numpy as np

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

# Load the input image
image = cv2.imread("C:\RACHNA\letsgoo.jpg")
cv2.imshow('Original',image)
cv2.waitKey(0)

# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_image', gray_image)
cv2.waitKey(0)

# Convert the region of interest to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
cv2.waitKey(0)

# Threshold the image to get only the red and green color ranges
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Count the number of pixels in the red and green color ranges
red_pixels = cv2.countNonZero(mask_red)
cv2.imshow('red_pixels',red_pixels)
cv2.waitKey(0)

green_pixels = cv2.countNonZero(mask_green)
cv2.imshow('green_pixels',green_pixels)
cv2.waitKey(0)


if red_pixels > green_pixels:
    print("low traffic")
else:
    print("heavy traffic")

# Window shown waits for any key pressing event
cv2.destroyAllWindows()

