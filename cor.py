import cv2

def get_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at: x={x}, y={y}")

image = cv2.imread("rahullll.jpg")
resized = cv2.resize(image, (512, 512))

cv2.imshow("Click to get coordinates", resized)
cv2.setMouseCallback("Click to get coordinates", get_coords)

cv2.waitKey(0)
cv2.destroyAllWindows()
