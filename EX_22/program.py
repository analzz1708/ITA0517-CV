
import cv2
import numpy as np

img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imwrite("output.jpeg", closing)

cv2.imshow("Original Image", img)
cv2.imshow("Morphological Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
