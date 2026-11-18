
import cv2

# Read the input image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: input.jpeg not found!")
    exit()

# Load the face detection classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("Error: Face detection model could not be loaded!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the face count
face_count = len(faces)

cv2.putText(
    img,
    "Faces: " + str(face_count),
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

# Save and display the result
cv2.imwrite("output.jpeg", img)
cv2.imshow("Face Detection and Counting", img)

print("Number of faces detected:", face_count)
print("Output saved as output.jpeg")

cv2.waitKey(0)
cv2.destroyAllWindows()
