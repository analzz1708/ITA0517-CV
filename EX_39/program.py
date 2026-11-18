
import cv2
import os
import shutil
import time

# Input and output video files
input_video = "input.mp4"
output_video = "output.mp4"
temp_folder = "temp_frames"

# Open the input video
cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Error: input.mp4 not found or could not be opened!")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 25

# Half speed for slow motion
output_fps = max(fps / 2, 1)

# Read and save all video frames
if os.path.exists(temp_folder):
    try:
        shutil.rmtree(temp_folder)
    except OSError:
        print("Close any program using the temp_frames folder, then try again.")
        cap.release()
        exit()

os.makedirs(temp_folder)

print("Reading video frames... Please wait.")

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_path = os.path.join(
        temp_folder, f"frame_{frame_count:08d}.jpg"
    )

    if not cv2.imwrite(frame_path, frame):
        print("Error saving a temporary frame.")
        cap.release()
        exit()

    frame_count += 1

cap.release()

if frame_count == 0:
    print("Error: No frames found in the video!")
    exit()

print("Creating reverse slow-motion video...")

# Create output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    output_video, fourcc, output_fps, (width, height)
)

if not out.isOpened():
    print("Error: Could not create output.mp4")
    exit()

# Write frames in reverse order
for i in range(frame_count - 1, -1, -1):
    frame_path = os.path.join(
        temp_folder, f"frame_{i:08d}.jpg"
    )

    frame = cv2.imread(frame_path)

    if frame is not None:
        out.write(frame)

out.release()

print("Reverse slow-motion video created!")
print("Output saved as output.mp4")

# Clean up temporary frames; don't crash if Windows blocks deletion
try:
    shutil.rmtree(temp_folder)
    print("Temporary files cleaned up.")
except OSError:
    print("Note: temp_frames could not be deleted. You can delete it later.")

# Play the output video
video = cv2.VideoCapture(output_video)

if video.isOpened():
    delay = max(1, int(1000 / output_fps))

    while True:
        ret, frame = video.read()

        if not ret:
            break

        cv2.imshow("Reverse Slow Motion Video - Press Q to Quit", frame)

        if cv2.waitKey(delay) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()
else:
    print("Output video was saved, but could not be opened for playback.")
