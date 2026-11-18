
import cv2

# Read the input image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

# Resize image to a bigger size
bigger = cv2.resize(
    img,
    None,
    fx=2,
    fy=2,
    interpolation=cv2.INTER_CUBIC
)

# Resize image to a smaller size
smaller = cv2.resize(
    img,
    None,
    fx=0.5,
    fy=0.5,
    interpolation=cv2.INTER_AREA
)

# Save output images
cv2.imwrite("bigger.jpeg", bigger)
cv2.imwrite("smaller.jpeg", smaller)

# Display original and resized images
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image scaling completed successfully!")
