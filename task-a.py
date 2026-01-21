import cv2
import matplotlib.pyplot as plt
# Path to the image
image_path = "images/colourimg.jpg"

# Load image (BGR by default)
img = cv2.imread(image_path)

# Safety check
if img is None:
    print(f"Error: Could not load image at {image_path}")
    exit(1)

# Print image information
print("Image loaded successfully")
print("Image shape (H, W, C):", img.shape)
print("Data type:", img.dtype)

# Convert BGR to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("My Image")
plt.axis("off")
plt.show()

# Split channels (still from BGR image)
b_channel, g_channel, r_channel = cv2.split(img)

