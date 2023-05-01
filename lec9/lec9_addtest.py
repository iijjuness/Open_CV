import cv2
import numpy as np
import glob
import os

airplane = cv2.imread('lec9_airplane.bmp')
field = cv2.imread('lec9_field.bmp')

ii = np.arange(0, 2, 0.05)
array = []
for i in ii:
    alpha = i
    for j in ii:
        beta = j
        dst = cv2.addWeighted(field, alpha, airplane, beta, 0)

    out = cv2.imwrite('1.bmp', dst)
    array.append(out)

print(array)