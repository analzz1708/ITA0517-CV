
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

video = cv2.VideoCapture("input.mp4")

if not video.isOpened():
    print("Video not found!")
    exit()

text_list = []
count = 0

while True:
    ret, frame = video.read()

    if not ret:
        break

    if count % 30 == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray).strip()

        if text and text not in text_list:
            text_list.append(text)

    count += 1

video.release()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(text_list))

print("Text extracted successfully!")
print("Saved in output.txt")
