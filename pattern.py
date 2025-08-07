import cv2

# Step 1: Load the image (grayscale makes edge detection easier)
img = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)

# Step 2: Apply Gaussian Blur to reduce noise (optional but improves results)
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Step 3: Apply Canny Edge Detector
edges = cv2.Canny(blur, threshold1=10, threshold2=150)

# Step 4: Show the original and edge-detected images
cv2.imshow("Original", img)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
