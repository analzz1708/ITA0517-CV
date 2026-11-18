
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

# Calculate rectangle coordinates
start_point = (width // 4, height // 4)
end_point = (3 * width // 4, 3 * height // 4)

# Draw a blue rectangle
cv2.rectangle(
    img,
    start_point,
    end_point,
    (255, 0, 0),
    3
)

# Save and display the output
cv2.imwrite("output.jpeg", img)
cv2.imshow("White Image with Rectangle", img)

print("Rectangle created successfully!")
print("Output saved as output.jpeg")

cv2.waitKey(0)
cv2.destroyAllWindows()
