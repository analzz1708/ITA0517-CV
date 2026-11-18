
import cv2

input_video = "input.mp4"

# Open video
cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Error: Video not found!")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 30

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Create output video files
slow_out = cv2.VideoWriter(
    "slow_motion.mp4", fourcc, fps / 3, (width, height)
)

fast_out = cv2.VideoWriter(
    "fast_motion.mp4", fourcc, fps, (width, height)
)

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save every frame for slow motion
    slow_out.write(frame)

    # Save every third frame for fast motion
    if frame_count % 3 == 0:
        fast_out.write(frame)

    frame_count += 1

cap.release()
slow_out.release()
fast_out.release()

print("Slow motion and fast motion videos saved!")

# Display slow-motion video
cap = cv2.VideoCapture("slow_motion.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Slow Motion", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

# Display fast-motion video
cap = cv2.VideoCapture("fast_motion.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Fast Motion", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
