import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
img = cv2.line(img, (0,0), (511, 511), (255, 0, 0), 5)
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

pts = np.array([[50, 30], [100, 150], [350, 100], [250, 50]])
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()