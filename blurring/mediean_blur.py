import cv2

read_img=cv2.imread("rahul.png")

#resize
img=cv2.resize(read_img,(800,800),interpolation=cv2.INTER_AREA)


ksize=(25)

blur=cv2.medianBlur(img,ksize)






cv2.imshow("image",img)
cv2.imshow("blur",blur)

cv2.waitKey(0)

cv2.destroyAllWindows()







