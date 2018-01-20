import numpy as np
import cv2


#Used to remove background and check difference between frames to detect motion
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('mask', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
