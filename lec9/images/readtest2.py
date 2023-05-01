import cv2

delay = int(1000/20)
video = cv2.VideoCapture('hw3___000.avi')

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
video_out = cv2.VideoWriter('hw3_201900000.avi', fourcc, 20, (600, 400))

while True:
    ret, frame_v = video.read()

    if ret == False:
        print("Failed to call video")
        break

    str_1 = '201715475'

    cv2.putText(frame_v, str_1, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    video_out.write(frame_v)
    key = cv2.waitKey(delay)

    if key == 27:
        break

video.release()
cv2.destroyAllWindows()
