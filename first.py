import cv2

img=cv2.imread("image.png")
cv2.imshow("test",img)

cv2.waitKey(0)

cv2.destroyAllWindows

save_img=cv2.imwrite("new.png",img)





