import numpy as np
import cv2

cap1 = cv2.VideoCapture('lec5_video1.mp4')
cap2 = cv2.VideoCapture('lec5_video2.mp4')

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter('lec5_output.avi', fourcc, fps, (w, h))

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
effect_frames = int(fps * 2) # 2 sec

for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()
    out.write(frame1)
    cv2.imshow('output', frame1)
    cv2.waitKey(delay)

for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    dx = int(w/effect_frames) * i
    frame = np.zeros((h,w,3), dtype=np.uint8)

    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]

    out.write(frame)
    cv2.imshow('output', frame)
    cv2.waitKey(delay)

for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()
    out.write(frame2)
    cv2.imshow('output', frame2)
    cv2.waitKey(delay)




