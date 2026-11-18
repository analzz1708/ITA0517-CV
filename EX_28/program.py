
import cv2
import os

folder = os.path.dirname(os.path.abspath(__file__))

video_path = os.path.join(folder, "input.mp4")
prototxt_path = os.path.join(folder, "MobileNetSSD_deploy.prototxt.txt")
model_path = os.path.join(folder, "MobileNetSSD_deploy.caffemodel")
output_path = os.path.join(folder, "output.mp4")

for path in [video_path, prototxt_path, model_path]:
    if not os.path.isfile(path):
        print("File not found:", os.path.basename(path))
        raise SystemExit

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

classes = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow",
    "diningtable", "dog", "horse", "motorbike", "person",
    "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open input.mp4")
    raise SystemExit

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 25

out = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

if not out.isOpened():
    cap.release()
    print("Error: Cannot create output.mp4")
    raise SystemExit

while True:
    ret, frame = cap.read()
    if not ret:
        break

    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)),
        0.007843,
        (300, 300),
        127.5
    )

    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = float(detections[0, 0, i, 2])

        if confidence > 0.45:
            class_id = int(detections[0, 0, i, 1])

            if class_id >= len(classes):
                continue

            if classes[class_id] not in ["car", "bus", "motorbike", "bicycle", "train"]:
                continue

            box = detections[0, 0, i, 3:7] * [
                width, height, width, height
            ]
            x1, y1, x2, y2 = box.astype(int)

            x1 = max(0, min(x1, width - 1))
            x2 = max(0, min(x2, width - 1))
            y1 = max(0, min(y1, height - 1))
            y2 = max(0, min(y2, height - 1))

            label = f"{classes[class_id]}: {confidence:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame, label, (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
            )

    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()

print("Vehicle detection completed!")
print("Output saved as output.mp4")
