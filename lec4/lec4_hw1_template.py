import numpy as np
import cv2

img = cv2.imread('lec4_vehicles.jpg')
out = img.copy()
# To Do #
cv2.rectangle(out, (100,100), (150,170), (0,255,0), 2)

cv2.imwrite('hw1_output.jpg', out)

cv2.imshow('image', out)
cv2.waitKey(0)



