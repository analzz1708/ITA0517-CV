
import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: input.jpeg not found!")
    exit()

# Convert image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define orange color range
lower_orange = np.array([5, 40, 40])
upper_orange = np.array([30, 255, 255])

# Define purple color range
lower_purple = np.array([125, 30, 30])
upper_purple = np.array([170, 255, 255])

# Detect orange and purple foreground
orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)
purple_mask = cv2.inRange(hsv, lower_purple, upper_purple)

# Combine both color masks
foreground_mask = cv2.bitwise_or(orange_mask, purple_mask)

# Extract the selected foreground colors
foreground = cv2.bitwise_and(
    img, img, mask=foreground_mask
)

# Replace the remaining areas with white
background_mask = cv2.bitwise_not(foreground_mask)
white_background = np.full_like(img, 255)

background = cv2.bitwise_and(
    white_background, white_background,
    mask=background_mask
)

result = cv2.add(foreground, background)

# Save and display the output
cv2.imwrite("output.jpeg", result)

cv2.imshow("Original Image", img)
cv2.imshow("Extracted Foreground", result)

print("Foreground extraction completed!")
print("Output saved as output.jpeg")

cv2.waitKey(0)
cv2.destroyAllWindows()
