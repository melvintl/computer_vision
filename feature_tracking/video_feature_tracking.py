import numpy as np
import cv2

def good_feature_track(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray,125,0.01,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,255,-1)

    return img


def SIFT(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray,None)
    #kp, des = sift.detectAndCompute(gray,None)
    #flags is optional, try without and see what happens
    img=cv2.drawKeypoints(gray,kp, None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img


def SURF(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    surf = cv2.xfeatures2d.SURF_create(100) #Pass in a hessianThreshold value
    #surf.hessianThreshold = 50000
    kp = surf.detect(img,None)
    print(len(kp))
    #flags is optional, try without and see what happens
    #img=cv2.drawKeypoints(gray,kp, None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    img=cv2.drawKeypoints(gray,kp, None)
    
    return img

def fast_feature_detection(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fast = cv2.FastFeatureDetector_create(15)
    kp = fast.detect(img,None)
    img=cv2.drawKeypoints(gray,kp, None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #flags is optional, try without and see what happens
    #img=cv2.drawKeypoints(gray,kp, None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img

#Doest work!
def BRIEF(img):
    # Initiate STAR detector
    star = cv2.FeatureDetector_create("STAR")
    # Initiate BRIEF extractor
    brief = cv2.DescriptorExtractor_create("BRIEF")

    # find the keypoints with STAR
    kp = star.detect(img,None)

    # compute the descriptors with BRIEF
    kp, des = brief.compute(img, kp)
    img=cv2.drawKeypoints(gray,kp, None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #flags is optional, try without and see what happens
    #img=cv2.drawKeypoints(gray,kp, None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img

def ORB(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints with ORB
    kp = orb.detect(img,None)

    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)
    img=cv2.drawKeypoints(gray,kp, None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    img = ORB(img)

    cv2.imshow('dst',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
