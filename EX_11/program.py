
import cv2

img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

rotated = cv2.rotate(img, cv2.ROTATE_180)

cv2.imwrite("output.jpeg", rotated)

cv2.imshow("Original Image", img)
cv2.imshow("180 Degree Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
