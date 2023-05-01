import cv2
import numpy as np

img1 = cv2.imread('lenna.bmp', cv2.IMRAD_COLOR)
img2 = np.zeros((480, 640, 3), np.uint8)
img3 = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
img4 = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)