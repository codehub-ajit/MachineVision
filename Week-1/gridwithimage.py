import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("images/colourimg.jpg")

if img is None:
    print("Error: Could not load image")
    exit(1)
# Convert BGR to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Split channels (OpenCV uses BGR)
b, g, r = cv2.split(img)

# Create 2x2 grid
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Original image
axs[0, 0].imshow(img_rgb)
axs[0, 0].set_title("Original - YOUR NAME")
axs[0, 0].axis("off")

# Red channel
axs[0, 1].imshow(r, cmap="gray")
axs[0, 1].set_title("Red Channel")
axs[0, 1].axis("off")

# Green channel
axs[1, 0].imshow(g, cmap="gray")
axs[1, 0].set_title("Green Channel")
axs[1, 0].axis("off")

# Blue channel
axs[1, 1].imshow(b, cmap="gray")
axs[1, 1].set_title("Blue Channel")
axs[1, 1].axis("off")

plt.tight_layout()
plt.savefig("task-a-result.png")
plt.show()