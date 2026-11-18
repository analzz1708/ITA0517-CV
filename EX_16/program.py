
import cv2
import numpy as np

img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

abs_x = cv2.convertScaleAbs(sobel_x)
abs_y = cv2.convertScaleAbs(sobel_y)

output = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

cv2.imwrite("output.jpeg", output)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel Filter", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
