
import cv2

# Read the input image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: input.jpeg not found!")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Get threshold value from the user
threshold_value = int(input("Enter threshold value (0-255): "))

if threshold_value < 0 or threshold_value > 255:
    print("Enter a value between 0 and 255.")
    exit()

# Apply threshold segmentation
ret, segmented = cv2.threshold(
    gray, threshold_value, 255, cv2.THRESH_BINARY
)

# Save the segmented image
cv2.imwrite("output.jpeg", segmented)

# Display original and segmented images
cv2.imshow("Original Image", img)
cv2.imshow("Segmented Image", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image segmentation completed!")
print("Output saved as output.jpeg")
