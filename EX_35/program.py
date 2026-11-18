
import cv2

# Read the input image
img = cv2.imread("input.jpeg")

if img is None:
    print("Error: input.jpeg not found!")
    exit()

# Get text from the user
text = input("Enter the text to display on the image: ")

if not text.strip():
    print("Please enter some text.")
    exit()

# Choose text position and style
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2

# Add a dark background behind the text for visibility
(text_width, text_height), baseline = cv2.getTextSize(
    text, font, font_scale, thickness
)

x = 20
y = max(text_height + 20, 50)

cv2.rectangle(
    img,
    (x - 5, y - text_height - 10),
    (min(x + text_width + 5, img.shape[1] - 1), y + baseline + 5),
    (0, 0, 0),
    -1
)

# Write the text in white
cv2.putText(
    img,
    text,
    (x, y),
    font,
    font_scale,
    (255, 255, 255),
    thickness,
    cv2.LINE_AA
)

# Save and display the result
cv2.imwrite("output.jpeg", img)
cv2.imshow("Image with Text", img)

print("Text added successfully!")
print("Output saved as output.jpeg")

cv2.waitKey(0)
cv2.destroyAllWindows()
