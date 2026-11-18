
import cv2
import os

# Save files in the same folder as program.py
folder = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(folder, "input.mp4")
output_path = os.path.join(folder, "output.mp4")
temp_folder = os.path.join(folder, "temp_frames")

if not os.path.isfile(input_path):
    print("ERROR: input.mp4 not found in EX_26 folder!")
    raise SystemExit

cap = cv2.VideoCapture(input_path)

if not cap.isOpened():
    print("ERROR: Cannot open input.mp4")
    raise SystemExit

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 30

# Read frames and save them temporarily to avoid using too much RAM
os.makedirs(temp_folder, exist_ok=True)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_path = os.path.join(temp_folder, f"frame_{count:08d}.jpg")
    if not cv2.imwrite(frame_path, frame):
        cap.release()
        print("ERROR: Could not save temporary frame.")
        raise SystemExit

    count += 1

cap.release()

if count == 0:
    print("ERROR: No frames found in input.mp4")
    raise SystemExit

# Write frames in reverse order
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

if not out.isOpened():
    print("ERROR: Cannot create output.mp4. Check OpenCV codec support.")
    raise SystemExit

for i in range(count - 1, -1, -1):
    frame_path = os.path.join(temp_folder, f"frame_{i:08d}.jpg")
    frame = cv2.imread(frame_path)

    if frame is None:
        print("ERROR: Could not read frame", i)
        out.release()
        raise SystemExit

    out.write(frame)

out.release()

# Remove temporary frames after successful writing
for name in os.listdir(temp_folder):
    os.remove(os.path.join(temp_folder, name))
os.rmdir(temp_folder)

print("SUCCESS! Reverse video saved as output.mp4")
print("Total frames:", count)
print("Output location:", output_path)