import cv2

cap = cv2.VideoCapture(0)
print(cap.isOpened())

w = round( cap.get(cv2.CAP_PROP_FRAME_WIDTH) )
h = round( cap.get(cv2.CAP_PROP_FRAME_HEIGHT) )
fps = cap.get(cv2.CAP_PROP_FPS)  #fps: frames per second
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
delay = round(1000/fps)  # msec

out = cv2.VideoWriter('lec5_output.avi', fourcc, fps, (w,h))

mode = 0
while True:
    ret, frame = cap.read()
    inversed = ~frame  # 255 - i(x,y)

    key = cv2.waitKey(delay)
    if key == 27: # ESC
        break

    if key == ord('a') and mode == 0:    mode = 1
    if key == ord('b') and mode == 1:    mode = 0

    if mode == 0:
        out.write(frame)
        cv2.imshow('window', frame)
    else:
        out.write(inversed)
        cv2.imshow('window', inversed)

cap.release()
out.release()
