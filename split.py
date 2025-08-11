import cv2

img = cv2.imread("new.png")

b, g, r = cv2.split(img)

#cv2.imshow("image",img)

#cv2.imshow("Blue Channel ", b)
#cv2.imshow("Green Channel ", g)
#cv2.imshow("Red Channel ", r)



img2=cv2.merge((b,g,r))
cv2.imshow("merged",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

