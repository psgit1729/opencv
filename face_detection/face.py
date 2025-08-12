import cv2
import matplotlib.pyplot as plt

# Read the image in grayscale (0 flag)
read_img = cv2.imread("grp2.png",0)

# Resize to 800x800
img = cv2.resize(read_img, (800, 800), interpolation=cv2.INTER_AREA)



#### face detcetion using haar cascading

face_detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")







###calculate the coordinates of the face

faces_cordinate=face_detect.detectMultiScale(img,1.2,4)
print(faces_cordinate)


###drwa the rectangle on the face coordinate
for x,y,w,h in faces_cordinate:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)




cv2.imshow("face",img)

cv2.waitKey(0)

cv2.destroyAllWindows







