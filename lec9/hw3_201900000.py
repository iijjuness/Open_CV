import cv2
import numpy as np
import glob
from PIL import ImageFont, Image, ImageDraw
import os

airplane = cv2.imread('lec9_airplane.bmp')
field = cv2.imread('lec9_field.bmp')
fps = 20
path = '/Users/iijjuness/PycharmProjects/pythonProject3/lec9'

h, w, c = airplane.shape

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter('window.avi', fourcc, 20, (h, w))

ii = np.arange(0, 2, 0.05)
aW_array = []
for i in ii:
    # img = aW_array.append(cv2.addWeighted(field, i, airplane, 1 - i, 0))
    dst = cv2.addWeighted(field, i, airplane, 1 - i, 0)
    out = cv2.imwrite('1.bmp', dst)
    aW_array.append(out)


# while True:
#     rev = airplane.read()

    # str_1 = '201715475'
    # text = '이준승'
    # font = ImageFont.truetype("Gwangyang_Sunshine_Bold.ttf", 30)
    # img_pil = Image.fromarray(airplane)
    # draw = ImageDraw.Draw(img_pil)  # draw 객체 생성
    # draw.text((219, 22), text, (0, 255, 255), font=font)  # 글씨 쓰기
    # frame_w = np.array(img_pil)  # 다시 ndarray 형태로 변경

    # ii = np.arange(0, 2, 0.05)
    # aW_array = []
    # for i in ii:
    #     img = aW_array.append(cv2.addWeighted(field, i, airplane, 1 - i, 0))
        # dst = cv2.addWeighted(field, i, airplane, 1 - i, 0)
        # out = cv2.imwrite('1.bmp', dst)
        # aW_array.append(out)