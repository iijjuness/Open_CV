# import numpy as np
import cv2

# 리스트 정의
axis_l = []
axis_r = []

img = cv2.imread('lec4_vehicles.jpg')
out = img.copy()

# 사각형 그리는 함수
def draw_rectangle(event, x, y, flag, param):
    global ix, iy, jx, jy
    # 마우스 왼쪽 눌렸을 때 좌표값 axis_l 리스트에 저장
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        axis_l.append((ix, iy))
    # 마우스 오른쪽 눌렀을 때 좌표값 axis_r 리스트에 저장
    elif event == cv2.EVENT_RBUTTONDOWN:
        jx, jy = x, y
        axis_r.append((jx, jy))

    # axis_l의 값을 시작으로, axis_r의 값을 마지막으로 하는 사각형 그리기
    for i, j in zip(axis_l, axis_r):
        cv2.rectangle(out, (i[0], i[1]), (j[0], j[1]),
                      (0, 255, 0), 2)
        cv2.rectangle(img, (i[0], i[1]), (j[0], j[1]),
                      (0, 255, 9), 2)

        cv2.imwrite('hw1_output.jpg', out)
        cv2.imshow('lec4_vehicles.jpg', img)


cv2.imshow('lec4_vehicles.jpg', img)
cv2.setMouseCallback('lec4_vehicles.jpg', draw_rectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()



