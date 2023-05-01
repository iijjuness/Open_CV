import numpy as np
import cv2

def onChange(value):
    global img, title
    img[:] = value
    cv2.imshow(title, img)

title = "Trackbar Event"
img = np.zeros((300, 500), np.uint8)
cv2.namedWindow(title)
cv2.imshow(title, img)

cv2.createTrackbar("Brightness", title, 0, 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
