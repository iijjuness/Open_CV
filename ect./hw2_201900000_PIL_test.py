import numpy as np
import cv2
import time
from PIL import ImageFont, Image, ImageDraw


rain = cv2.VideoCapture('lec6_raining.mp4')  # rain에 불러온 동영상 저장
woman = cv2.VideoCapture('lec6_woman.mp4')  # woman에 불러온 동영상 저장

w = round(rain.get(cv2.CAP_PROP_FRAME_WIDTH))  # 영상 프레임 넓이
h = round(rain.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 영상 프레임 높이
fps_1 = rain.get(cv2.CAP_PROP_FPS)  # 영상 프레임 정의
delay = int(1000 /fps_1)  # delay 값 계산
frame_cnt_r = round(rain.get(cv2.CAP_PROP_FRAME_COUNT))  # rain 동영상의 프레임 수 계산
frame_cnt_w = round(woman.get(cv2.CAP_PROP_FRAME_COUNT))  # woman 동영상의 프레임 수 계산
prevTime = time.time()

fourcc = cv2.VideoWriter_fourcc(*"DIVX")  # 코덱
out = cv2.VideoWriter('hw2_201900000.mp4', fourcc, fps_1, (w, h))  # 저장할 동영상

# 마우스 이벤트로 좌표값 구하기
# def onMouse(event, x, y, flag, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         a = x
#         b = y
#         print(a, b)

chrk = False  # Chroma Key 정의
while True:
    ret_w, frame_w = woman.read()

    if ret_w == False:  # 영상을 읽지 못하면 종료
        break

    # 영상에 입력할 단어들
    str_1 = '201715475'
    str_2 = "Chroma Key Mode : "
    str_3 = "Off"
    str_4 = "On"

    # pillow 이용하여 한글 Text 입력
    text = "이준승"
    font = ImageFont.truetype("Gwangyang_Sunshine_Bold.ttf", 30)  # font는 광양햇살 볼드체로 설정
    # font = ImageFont.load_default()
    img_pil = Image.fromarray(frame_w)  # numpy array 타입 변경
    draw = ImageDraw.Draw(img_pil)  # draw 객체 생성
    draw.text((219, 22), text, (0, 255, 255), font=font)  # 글씨 쓰기
    frame_w = np.array(img_pil)  # 다시 ndarray 형태로 변경

    # 실시간 프레임 수 계산
    curTime = time.time()
    fps = 1 / (curTime - prevTime)
    prevTime = curTime
    fps_str = "fps : %.2lf" % fps

    # 프레임 카운트
    fi = "frame id : %.lf" % round(woman.get(cv2.CAP_PROP_POS_FRAMES))

    # 영상에 입력
    cv2.putText(frame_w, str_1, (23, 58), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame_w, str_2, (23, 208), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame_w, fps_str, (23, 108), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame_w, fi, (23, 158), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # 스페이스바를 누를 시 Chroma Key On / Off 판별
    if chrk == False:
        cv2.putText(frame_w, str_3, (350, 211), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    else:
        cv2.putText(frame_w, str_4, (350, 211), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Chroma Key True일 때 'frame_w'마스크 만들기
    if chrk:
        ret_r, frame_r = rain.read()

        hsv = cv2.cvtColor(frame_w, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
        cv2.copyTo(frame_r, mask, frame_w)

    out.write(frame_w)
    cv2.imshow(f'hw2_201900000.mp4', frame_w)
    key = cv2.waitKey(delay)

    # cv2.setMouseCallback('hw2_201900000.mp4', onMouse)

    # 스페이스바 입력시 Chroma Key 해제 및 적용 & ESC 입력시 영상 종료
    if key == ord(' '):
        chrk = not chrk
        str_3 = str_4
    elif key == 27:
        break

woman.release()
rain.release()
cv2.destroyAllWindows()






