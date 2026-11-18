
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

# Calculate box size (one-tenth of image dimensions)
box_width = width // 10
box_height = height // 10

# Draw four colored boxes at the corners
# OpenCV uses BGR color format
cv2.rectangle(img, (0, 0),
              (box_width - 1, box_height - 1),
              (0, 0, 0), -1)  # Black: top-left

cv2.rectangle(img, (width - box_width, 0),
              (width - 1, box_height - 1),
              (255, 0, 0), -1)  # Blue: top-right

cv2.rectangle(img, (0, height - box_height),
              (box_width - 1, height - 1),
              (0, 255, 0), -1)  # Green: bottom-left

cv2.rectangle(img, (width - box_width, height - box_height),
              (width - 1, height - 1),
              (0, 0, 255), -1)  # Red: bottom-right

# Save and display the image
cv2.imwrite("output.jpeg", img)
cv2.imshow("White Image with Four Colored Boxes", img)

print("Image created successfully!")
print("Output saved as output.jpeg")

cv2.waitKey(0)
cv2.destroyAllWindows()
