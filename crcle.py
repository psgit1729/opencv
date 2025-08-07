import numpy as np
import cv2

# Create a 100x100 black image (grayscale)
img = np.zeros((100, 100), dtype=np.uint8)

# Draw a white circle (value 255) at the center with radius 30
cv2.circle(img, center=(50, 50), radius=30, color=255, thickness=-1)

# Save or show the image
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
