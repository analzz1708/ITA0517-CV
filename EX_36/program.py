
import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: input.jpeg not found!")
    exit()

# Convert image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define green color range
lower_green = np.array([25, 30, 30])
upper_green = np.array([95, 255, 255])

# Detect the green background
background_mask = cv2.inRange(hsv, lower_green, upper_green)

# Keep the non-green parts of the image
foreground_mask = cv2.bitwise_not(background_mask)

# Create a white background
white_background = np.full_like(img, 255)

# Keep the foreground and replace green areas with white
foreground = cv2.bitwise_and(img, img, mask=foreground_mask)
background = cv2.bitwise_and(
    white_background, white_background, mask=background_mask
)
result = cv2.add(foreground, background)

# Save and display the result
cv2.imwrite("output.jpeg", result)
cv2.imshow("Original Image", img)
cv2.imshow("Background Removed", result)

print("Background subtraction completed!")
print("Output saved as output.jpeg")

cv2.waitKey(0)
cv2.destroyAllWindows()
