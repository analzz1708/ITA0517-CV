
import cv2

# Read the input image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

# Rotate the image 90 degrees clockwise
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Save the output image
cv2.imwrite("output.jpeg", rotated)

# Display original and rotated images
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image - 90 Degrees Clockwise", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Rotated image saved successfully!")
