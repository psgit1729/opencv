import cv2
import matplotlib.pyplot as plt


#### read image from folder

img=cv2.imread("image.png")


### apply histogram function

hist=cv2.calcHist([img],[0],None,[256],[0,266])


## plot the histogram
plt.plot(hist)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
