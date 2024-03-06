import cv2
import numpy as np

image = cv2.imread("images/clear/IMG_20240304_182842.jpg")
image = cv2.resize(image, (1200, 900))
im_copy = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# 2. colour area for matches in HSV colourspace
lower_b = np.array([15, 53, 60])
upper_b = np.array([179, 255, 255])

# create a mask
mask = cv2.inRange(im_copy, lower_b, upper_b)

# change color by mask
image[mask>0] = (0, 0, 255)

cv2.imshow("Image", image)  
cv2.waitKey(6000)
cv2.destroyAllWindows()