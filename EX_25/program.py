
import cv2

img = cv2.imread("input.jpeg")
template = cv2.imread("watch_template.jpeg")

if img is None or template is None:
    print("Error: Input image or watch template not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

h, w = template_gray.shape

result = cv2.matchTemplate(
    gray, template_gray, cv2.TM_CCOEFF_NORMED
)

_, max_value, _, max_location = cv2.minMaxLoc(result)

if max_value > 0.6:
    top_left = max_location
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    print("Watch detected!")
else:
    print("Watch not detected. Try a better template image.")

cv2.imwrite("output.jpeg", img)
cv2.imshow("Watch Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
