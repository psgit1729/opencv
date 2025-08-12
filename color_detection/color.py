import cv2
import numpy as np

read_img=cv2.imread("rahul.png")

img=cv2.resize(read_img,(800,800),interpolation=cv2.INTER_AREA)

### convert to hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower=np.array([240,100,100])
upper=np.array([280,255,255])


mask=cv2.inRange(hsv,lower,upper)
print(mask)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         


cv2.imshow("original",img)
cv2.imshow("original image",mask)

cv2.waitKey(0)

cv2.destroyAllWindows()





