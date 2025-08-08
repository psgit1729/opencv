import cv2

read_img=cv2.imread("rahul.png")

img=cv2.resize(read_img,(800,800),interpolation=cv2.INTER_AREA)



####canny
canny=cv2.Canny(img,100,150)



cv2.imshow("image",img)
cv2.imshow("edges",canny)



cv2.waitKey(0)

cv2.destroyAllWindows







