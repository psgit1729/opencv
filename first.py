import cv2

read_img=cv2.imread("rahul.png")

img=cv2.resize(read_img,(800,800),interpolation=cv2.INTER_AREA)




cv2.imshow("original",img)

cv2.waitKey(0)

cv2.destroyAllWindows()





