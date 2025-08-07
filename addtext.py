#### adding text


import cv2

img=cv2.imread("image.png")



img2=cv2.putText(img,"I am rahul",(200,200),cv2.FONT_HERSHEY_COMPLEX,0.5 ,(255,0,0),5)

cv2.imshow("nwe",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()