
import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

# Create a blank image for histogram
height = 400
width = 512
histogram_image = np.zeros((height, width, 3), dtype=np.uint8)

# Blue, Green and Red color channels
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Calculate and draw color histograms
for channel, color in enumerate(colors):
    hist = cv2.calcHist([img], [channel], None, [256], [0, 256])
    hist = cv2.normalize(
        hist, None, 0, 350, cv2.NORM_MINMAX
    ).flatten()

    for i in range(1, 256):
        x1 = (i - 1) * 2
        x2 = i * 2

        y1 = height - 1 - int(hist[i - 1])
        y2 = height - 1 - int(hist[i])

        cv2.line(
            histogram_image,
            (x1, y1),
            (x2, y2),
            color,
            2
        )

# Save output image
cv2.imwrite("output.jpeg", histogram_image)

# Display original image and histogram
cv2.imshow("Original Image", img)
cv2.imshow("Color Histogram", histogram_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Histogram output saved successfully!")
