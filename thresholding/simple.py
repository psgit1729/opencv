import cv2

import matplotlib.pyplot as plt


### read image

read_img=cv2.imread("rahul.png",0)


## resixe image
img=cv2.resize(read_img,(900,800),interpolation=cv2.INTER_AREA)


#### create a histogram to identify the threshold manually
'''
hist=cv2.calcHist([img],[0],None,[256],[0,255])


plt.plot(hist)
plt.show()
'''

###### Simple thresholding

### Binary Thresholding
ret,binary_thresh=cv2.threshold(img,72,255,cv2.THRESH_BINARY)

### Binary threshold Inverse

rest,binary_thresh_inv=cv2.threshold(img,72,255,cv2.THRESH_BINARY_INV)

### Trunc Threshold

rest,trunc_threshold=cv2.threshold(img,72,255,cv2.THRESH_TRUNC)

#### Trunc Threshold 
rest,zero_threshold=cv2.threshold(img,72,255,cv2.THRESH_TOZERO)


#### Trunc Threshold ZERO
rest,zero_threshold_inv=cv2.threshold(img,72,255,cv2.THRESH_TOZERO_INV)



cv2.imshow("binary thresholding",binary_thresh)
cv2.imshow("binary thresholding INV",binary_thresh_inv)
cv2.imshow("Trunc Threshold",trunc_threshold)
cv2.imshow("ZERO Threshold ",zero_threshold)
cv2.imshow("ZERO Threshold INV",zero_threshold_inv)


cv2.waitKey(0)
cv2.destroyAllWindows()