import cv2

image=cv2.imread("rahullll.jpg")
resize_img=cv2.resize(image,(800,800))
pixel=image.shape
cv2.imshow("resizexd",resize_img)
#print(pixel)

### modify faces y=[100,140] x=[240,294]   x=240,y=100  , x=240,y=140    , x=290,y=100  , x=290,y=140

select_img=image[100:140, 240:290]
#print(select_img.shape)
cv2.imshow("select",select_img)

b,g,r=cv2.split(select_img)
#print(b,g,r)

b1=b
g1=g
r1=r

merge_img=cv2.merge((b1,g1,r1))
#cv2.imshow("merged",merge_img)

resize_img[100:140, 240:290]=merge_img


cv2.imshow("Modified Image", resize_img)

#cv2.imshow("image",resize_img)

cv2.waitKey(0)
cv2.destroyAllWindows()




