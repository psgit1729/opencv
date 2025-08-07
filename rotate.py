import cv2


img=cv2.imread("image.png")

### rotae using rotation amtrix
print(img.shape)
h,w,p=img.shape
s=(h,w)
m=cv2.getRotationMatrix2D(center=s,angle=-90,scale=1)

output=cv2.warpAffine(img,m,dsize=s)

img2=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("imag",img)

cv2.imshow("Roatedimag",output)
cv2.imshow("Roatedimag",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
