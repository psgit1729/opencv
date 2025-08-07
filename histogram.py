import cv2
import matplotlib.pylab as plt
img=cv2.imread("new.png")

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



#h,s,v=cv2.split(hsv)

his_hue=cv2.calcHist([hsv],[0],None,[180],[0,180])
his_sat=cv2.calcHist([hsv],[1],None,[256],[0,255])
his_value=cv2.calcHist([hsv],[2],None,[256],[0,255])


plt.plot(his_hue,color="red")
plt.plot(his_sat,color="green")
plt.plot(his_value,color="blue")
plt.show()4
cv2.imshow("hsv",hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
