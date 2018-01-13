import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('Img1.jpg',0)          # queryImage
img2 = cv2.imread('Img2.jpg',0) # trainImage

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create() #SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

matchesMask = [[0,0] for i in range(len(matches))]

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)

# cv2.drawMatchesKnn expects list of lists as matches.
#img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,flags=2)
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
#img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,**draw_params)


plt.imshow(img3),plt.show()