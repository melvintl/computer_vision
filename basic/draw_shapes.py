import cv2
import numpy as np

img = cv2.imread('/Users/melvinl/Downloads/STR-078z.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (150, 150), (255, 0, 0), 2)
cv2.rectangle(img, (0, 0), (150, 150), (0, 0, 255), 2)
cv2.circle(img, (100, 75), 55,  (0, 0, 255), 2)
pts = np.array( [[10, 5], [120, 30], [130, 140]], np.int32)

fonts = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, 'Some text', (0, 130), fonts, 1, (200, 200, 200, 3))

cv2.polylines(img, [pts], True, (0, 0, 255), 3)
cv2.imshow('Some image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
