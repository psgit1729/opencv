import cv2
import matplotlib.pyplot as plt


#### read image from folder

img=cv2.imread("red.png")


### apply histogram function
x=[0,1,2]
store_his=[]

for i in x:
    hist=cv2.calcHist([img],[i],None,[256],[0,266])
    store_his.append(hist)
    
    
#plot the graph individually

plt.plot(store_his[0],color="blue")
plt.plot(store_his[1],color="green")
plt.plot(store_his[2],color="red")

#plt.plot(hist)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
