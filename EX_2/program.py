import cv2

img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

blur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imwrite("output.jpeg", blur)

cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()