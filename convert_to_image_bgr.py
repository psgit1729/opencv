import cv2
import numpy as np

gbr_img = np.array([
    [[255,   0,   0], [  0, 255,   0], [  0,   0, 255]],  # R, G, B
    [[100, 100, 100], [255, 255, 255], [  0,   0,   0]],  # gray, white, black
    [[ 50, 100, 150], [ 90, 60, 30], [10, 20, 30]]        # custom colors
], dtype=np.uint8)
bgr_img = cv2.cvtColor(gbr_img, cv2.COLOR_RGB2BGR)
image=cv2.imwrite("convertedimage.png",bgr_img)


convertedimage=cv2.imread("convertedimage.png",1)
cv2.imshow("image",convertedimage)
cv2.waitKey(0)
cv2.destroyAllWindows