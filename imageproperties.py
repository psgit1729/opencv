import cv2 

img=cv2.imread("image.png")

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows


### properties

##shape

shape=img.shape
print(shape)
print(tuple(reversed(shape)))


###datatype
print(img.dtype)


###pixel size
print(img.size)



### print the array
print(img)