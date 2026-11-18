import cv2

# Read the image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert the original image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized = cv2.equalizeHist(gray)

# Save the equalized image
cv2.imwrite("output.jpeg", equalized)

# Compare original and equalized images
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Histogram Equalized Image", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()