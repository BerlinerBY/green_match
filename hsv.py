import cv2
import numpy as np
 
# Small app for picke HSV color space

def nothing(x):
    pass
  

cv2.namedWindow('image')
 
cv2.createTrackbar('lowH','image',0,179,nothing)
cv2.createTrackbar('highH','image',179,179,nothing)
 
cv2.createTrackbar('lowS','image',0,255,nothing)
cv2.createTrackbar('highS','image',255,255,nothing)
 
cv2.createTrackbar('lowV','image',0,255,nothing)
cv2.createTrackbar('highV','image',255,255,nothing)
 
while(True):
    frame = cv2.imread("images/clear/IMG_20240304_182842.jpg")
    frame = cv2.resize(frame, (800, 600))


    # get current positions of the trackbars
    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')
    
    # convert color to hsv 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    # create a mask
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    # reverse mask
    frame = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('image', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Press q to exit
        print(lower_hsv)
        print(higher_hsv)
        break
 
cv2.destroyAllWindows()