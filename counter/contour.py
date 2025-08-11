import cv2

# Read and resize
img = cv2.imread("apple.png")


# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding
_, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Draw all contours in green, thickness = 3
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)



#### Find the number of contours
num_contours = len(contours)
print(num_contours)


###  Calculate area  
for i, contour in enumerate(contours):     #### loop since it is a LIST
    area = cv2.contourArea(contour)
    print(f"Area of contour {i}: {area}")


#### Calculate perimeter
for i, contour in enumerate(contours):
    perimeter = cv2.arcLength(contour, True)  # True because contours are usually closed
    print(f"Perimeter of contour {i}: {perimeter}")





# Show results
cv2.imshow("Original + Contours", img)
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
