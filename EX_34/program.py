
import cv2
import numpy as np

# Get image size from the user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

if width < 10 or height < 10:
    print("Width and height must be at least 10.")
    exit()

# Create a white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Find the center of the image
center = (width // 2, height // 2)

# Set circle radius
radius = min(width, height) // 4

# Draw a red circle
cv2.circle(img, center, radius, (0, 0, 255), 3)

# Save and display the output
cv2.imwrite("output.jpeg", img)
cv2.imshow("White Image with Circle", img)

print("Circle created successfully!")
print("Output saved as output.jpeg")

cv2.waitKey(0)
cv2.destroyAllWindows()
