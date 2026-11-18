
import cv2

img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

height, width = img.shape[:2]

# Select a region of interest
x1 = width // 4
y1 = height // 4
x2 = 3 * width // 4
y2 = 3 * height // 4

roi = img[y1:y2, x1:x2]

# Save cropped region
cv2.imwrite("output.jpeg", roi)

# Copy the selected region and paste it into another image
result = img.copy()
result[0:roi.shape[0], 0:roi.shape[1]] = roi

cv2.imwrite("pasted.jpeg", result)

cv2.imshow("Original Image", img)
cv2.imshow("Cropped ROI", roi)
cv2.imshow("Copied and Pasted ROI", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
