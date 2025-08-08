import cv2

read_img=cv2.imread("rahul.png",0)


img=cv2.resize(read_img,(800,900),interpolation=cv2.INTER_AREA)



#### apply threshold
res,gau_thresh=cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)





cv2.imshow("otsu",gau_thresh)

cv2.waitKey(0)

cv2.destroyAllWindows()







