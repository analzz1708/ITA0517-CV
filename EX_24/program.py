
import cv2
import numpy as np

img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

kernel = np.ones((5, 5), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imwrite("output.jpeg", blackhat)

cv2.imshow("Original Image", img)
cv2.imshow("Black Hat Image", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
