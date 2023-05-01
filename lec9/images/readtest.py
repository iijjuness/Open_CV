import cv2
from PIL import ImageFont, ImageDraw
import numpy as np
from PIL import Image

img1 = cv2.imread('lec9_airplane.bmp')
img2 = cv2.imread('lec9_field.bmp')

delay = int(1000/20)

# # 마우스 이벤트로 좌표값 구하기
# def onMouse(event, x, y, flag, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         a = x
#         b = y
#         print(a, b)

alpha = 0  # alpha값 설정

added_images = []  # 이미지 저장할 리스트 생성

for i in range(60):
    beta = 1 - alpha  # beta값 설정
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)  # addWeighted 함수
    added_images.append(output)  # 함수 출력 결과물 리스트에 하나씩 추가
    alpha += (1 / 60)  # 알파값 증가
# print(output_images)

# 생성한 이미지 리스트 앞과 뒤에 추가
for j in range(20):
    added_images.insert(0, img2)
    added_images.append(img1)

fourcc = cv2.VideoWriter_fourcc(*"DIVX")  # 코덱
out = cv2.VideoWriter('hw3___000.avi', fourcc, 20, (600, 400))  # 저장할 동영상

# 만들어준 동영상 파일에 이미지 하나씩 삽입
for frame in added_images:
    out.write(frame)

out.release()

# 생성한 동영상 새로운 변수로 불러 오기
video = cv2.VideoCapture('hw3___000.avi')

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
video_out = cv2.VideoWriter('hw3_201900000.avi', fourcc, 20, (600, 400))

while True:
    ret, frame_v = video.read()

    if ret == False:
        print("Failed to call video")
        break

    # 동영상에 삽입할 변수 설정
    str_1 = '201715475'
    text = "이준승"

    font = ImageFont.truetype("Gwangyang_Sunshine_Bold.ttf", 30)  # font는 광양햇살 볼드체로 설정
    # font = ImageFont.load_default()
    img_pil = Image.fromarray(frame_v)  # numpy array 타입 변경
    draw = ImageDraw.Draw(img_pil)  # draw 객체 생성
    draw.text((208, 15), text, (0, 255, 255), font=font)  # 글씨 쓰기
    frame_v = np.array(img_pil)  # 다시 ndarray 형태로 변경

    # str_1 삽입
    cv2.putText(frame_v, str_1, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    video_out.write(frame_v)
    cv2.imshow('window', frame_v)
    key = cv2.waitKey(delay)

    if key == 27:
        break

video.release()
cv2.destroyAllWindows()

