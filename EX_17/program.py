
import cv2

img = cv2.imread("input.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

watermarked = img.copy()

text = "COMPUTER VISION"

cv2.putText(
    watermarked,
    text,
    (20, img.shape[0] - 20),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

cv2.imwrite("output.jpeg", watermarked)

cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()
