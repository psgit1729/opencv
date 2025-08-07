import cv2

import numpy as np


img=cv2.imread("image.png")


#cv2.imshow("image",img)

trim=img[40:49,18:49]
rev=(trim * 0.5).astype(np.uint8)





cv2.imshow("image1",trim)
cv2.imshow("image2",rev)

cv2.waitKey(0)
cv2.destroyAllWindows