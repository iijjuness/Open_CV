import numpy as np
import cv2

axis_l = []
axis_r = []

img = cv2.imread('lec4_vehicles.jpg')
out = img.copy()

def draw_rectangle(event, x, y, flag, param):
    global ix, iy, jx, jy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        axis_l.append((ix, iy))
    elif event == cv2.EVENT_RBUTTONDOWN:
        jx, jy = x, y
        axis_r.append((jx, jy))

    for i, j in zip(axis_l, axis_r):
        cv2.rectangle(img, (i[0], i[1]), (j[0], j[1]),
                      (0, 255, 0), 2)
        cv2.imshow('lec4_vehicles.jpg', img)

cv2.imshow('lec4_vehicles.jpg', img)
cv2.setMouseCallback('lec4_vehicles.jpg', draw_rectangle)

# 이미지 복사 후 저장
cv2.imwrite('hw1_output.jpg', out)
cv2.waitKey(0)
# while True:
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('a'):
#     elif k == 27:
#         break
cv2.destroyAllWindows()



