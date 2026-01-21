import cv2

img = cv2.imread("images/robodk_snapshot.png")

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Pixel clicked at: x={x}, y={y}")

cv2.imshow("Click to get pixel coordinates", img)
cv2.setMouseCallback("Click to get pixel coordinates", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
