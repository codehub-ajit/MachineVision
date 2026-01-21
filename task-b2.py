import cv2

# -------------------------------------------------
# Load RoboDK snapshot
# -------------------------------------------------
image_path = "images/robodk_snapshot.png"
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load RoboDK snapshot")
    exit(1)

# Print image information
print("Image shape (H, W, C):", img.shape)

# -------------------------------------------------
# Rectangle 1: Box
# Coordinates from pixel clicks
# Top-left  : (401, 434)
# Bottom-right: (609, 696)
# -------------------------------------------------
cv2.rectangle(img, (401, 434), (609, 696), (255, 0, 0), 2)
cv2.putText(
    img,
    "Box",
    (401, 420),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 0, 0),
    2
)

# -------------------------------------------------
# Rectangle 2: Mosaic Tile
# Coordinates from pixel clicks
# Top-left  : (848, 581)
# Bottom-right: (939, 669)
# -------------------------------------------------
cv2.rectangle(img, (848, 581), (939, 669), (0, 255, 0), 2)
cv2.putText(
    img,
    "Mosaic Tile",
    (848, 565),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 255, 0),
    2
)

# -------------------------------------------------
# Name and date (MANDATORY)
# -------------------------------------------------
cv2.putText(
    img,
    "Ajit G C - 2026-01-21",
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 0, 0),
    2
)

# -------------------------------------------------
# Save and display result
# -------------------------------------------------
output_path = "images/robodk_annotated.png"
cv2.imwrite(output_path, img)

print("Annotated image saved at:", output_path)

cv2.imshow("RoboDK Annotation", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()
