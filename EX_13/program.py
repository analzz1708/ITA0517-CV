
import cv2
import numpy as np

img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

rows, cols = img.shape[:2]

src_points = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

dst_points = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

matrix = cv2.getAffineTransform(src_points, dst_points)

transformed = cv2.warpAffine(img, matrix, (cols, rows))

cv2.imwrite("output.jpeg", transformed)

cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformation", transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
