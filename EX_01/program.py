
import cv2

# Read the image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save output image
cv2.imwrite("output.jpeg", gray)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
