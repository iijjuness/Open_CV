import numpy as np
import cv2


def onMouse(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        a = x
        b = y
        print(a, b)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Reft Butten pressed")

img = np.full((300, 500), 255, np.uint8)
title = "window"
cv2.imshow(title, img)

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
