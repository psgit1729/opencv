import cv2
import matplotlib.pyplot as plt


## read the file

img=cv2.imread("image.png",0)  ### convert to grayscale


### conver to histogramh    

hist=cv2.calcHist([img],[0],None,[256],[0,255])


### plot the histogram

plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()