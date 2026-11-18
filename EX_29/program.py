
import cv2

img = cv2.imread("input.jpeg")

if img is None:
    print("Error: input.jpeg not found!")
    exit()

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

if face_cascade.empty() or eye_cascade.empty():
    print("Error: Haar Cascade files could not be loaded!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50)
)

for (x, y, w, h) in faces:
    face_gray = gray[y:y+h, x:x+w]
    face_color = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(
        face_gray, scaleFactor=1.1, minNeighbors=5, minSize=(15, 15)
    )

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(
            face_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2
        )

cv2.imwrite("output.jpeg", img)

cv2.imshow("Eye Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Eye detection completed! Output saved as output.jpeg")
