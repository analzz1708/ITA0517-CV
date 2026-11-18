
import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(img, kernel, iterations=1)

# Save output image
cv2.imwrite("output.jpeg", eroded)

# Display original and eroded images
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Eroded image saved successfully!")
