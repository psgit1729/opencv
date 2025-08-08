import cv2
import matplotlib.pyplot as plt

read_img=cv2.imread("rahul.png",0)

### resize
img=cv2.resize(read_img,(800,900),interpolation=cv2.INTER_AREA)

'''
## Craet histogram to chk manually
hist=cv2.calcHist([img],[0],None,[256],[0,255])

plt.plot(hist)
plt.show()

'''
#### Adaptive thresolding

ad_thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,51,4)


cv2.imshow("adaptive",ad_thresh)


cv2.waitKey(0)

cv2.destroyAllWindows()







