import cv2 


image=cv2.imread("image.png")

print(image.shape)
scale=1.4
width=int(image.shape[1]*scale)
height=int(image.shape[0]*scale)


new=(width,height)

resize_img=cv2.resize(image,(800,1000),interpolation=cv2.INTER_CUBIC)
print(resize_img.shape)
cv2.imshow("image",image)
cv2.imshow("resized",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()