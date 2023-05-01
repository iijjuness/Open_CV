import numpy as np
import cv2
import time
from PIL import ImageFont, ImgaeDraw, Image

rain = cv2.VideoCapture('lec6_raining.mp4')
woman = cv2.VideoCapture('lec6_woman.mp4')

w = round(rain.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(rain.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps_1 = rain.get(cv2.CAP_PROP_FPS)
delay = int(1000 /fps_1)
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
frame_cnt_r = round(rain.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt_w = round(woman.get(cv2.CAP_PROP_FRAME_COUNT))
prevTime = time.time()


# out = cv2.VideoWriter('hw2_201900000_test.mp4', fourcc, fps_1, (w, h))

def onMouse(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        a = x
        b = y
        print(a, b)

chrk = False
while True:
    ret_w, frame_w = woman.read()
    str_1 = '201715475 이준승'
    str_2 = "Chroma Key Mode : "
    str_3 = "Off"
    str_4 = "On"

    curTime = time.time()
    fps = 1 / (curTime - prevTime)
    prevTime = curTime
    fps_str = "fps : %.2lf" % fps

    cv2.putText(frame_w, str_1, (23, 58), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame_w, fps_str, (28, 108), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame_w, str_2, (32, 167), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    if chrk == False:
        cv2.putText(frame_w, str_3, (363, 175), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    else:
        cv2.putText(frame_w, str_4, (363, 175), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    if chrk:
        ret_r, frame_r = rain.read()


        hsv = cv2.cvtColor(frame_w, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
        cv2.copyTo(frame_r, mask, frame_w)

    # cv2.imshow('hw2_201900000', frame_w)
    cv2.imshow('hw2_201900000', frame_w)

    key = cv2.waitKey(delay)

    # cv2.setMouseCallback('hw2_201900000', onMouse)
    cv2.setMouseCallback('hw2_201900000', onMouse)

    if key == ord(' '):
        chrk = not chrk
        str_3 = str_4
    elif key == 27:
        break

woman.release()
rain.release()
cv2.destroyAllWindows()






