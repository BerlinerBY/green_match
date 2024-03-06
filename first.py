import cv2
import numpy as np

#1
image = cv2.imread("images/clear/IMG_20240304_182842.jpg")
image = cv2.resize(image, (1200, 900))

#2
base = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(base, (13, 13), 0)

#3
th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,9,2)
contours, hierarchy = cv2.findContours(th3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#4
contour = np.zeros_like(image)

for i in range(len(contours)):
    # Exclude contours with a hierarchy value of [-1, -1, -1, -1]
    if hierarchy[0][i][3] != -1:
        cv2.fillConvexPoly(contour, contours[i], color=(255, 255, 255))

#5
im_floodfill = contour.copy()
h, w = contour.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)
cv2.floodFill(im_floodfill, mask, (0,0), 255)

#6
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
im_out = contour | im_floodfill_inv


#7
mask_white = cv2.inRange(im_out, 
                        lowerb=np.array([255, 255, 254]), 
                        upperb=np.array([255, 255, 255]))

im_copy = image.copy()
im_copy[mask_white>0] = (0, 0, 255)



cv2.imshow("4", im_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
