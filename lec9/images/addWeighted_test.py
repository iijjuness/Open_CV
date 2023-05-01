import cv2
import os
import glob
from PIL import ImageFont, Image, ImageDraw
import numpy as np
# # read two images
img1 = cv2.imread('lec9_airplane.bmp')
img2 = cv2.imread('lec9_field.bmp')
#
# # set alpha value
# alpha = 0
#
# # create an empty list to store output images
# output_images = []
#
# # loop through a range of values for alpha
# for i in range(60):
#     # calculate beta value
#     beta = 1 - alpha
#
#     # apply addWeighted
#     output = cv2.addWeighted(img1, alpha, img2, beta, 0)
#
#     # append output to list
#     output_images.append(output)
#
#     # increment alpha value
#     alpha += (1 / 60)
#
#
# # print(output_images)
# # display the output images
# for i, output in enumerate(output_images):
#     cv2.imwrite(f'{i}.bmp', output)
#     cv2.imshow(f'Output {i}', output)
#     cv2.waitKey()
#
# cv2.destroyAllWindows()

# # 마우스 이벤트로 좌표값 구하기
# def onMouse(event, x, y, flag, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         a = x
#         b = y
#         print(a, b)
#
# str_1 = '201715475'
# cv2.imshow('window', img1)
#
#
# cv2.setMouseCallback('window', onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


path = '/Users/iijjuness/PycharmProjects/pythonProject3/lec9/images'
out_path = '/Users/iijjuness/PycharmProjects/pythonProject3/lec9/images'
out_video_name = 'fading cube2.mp4'
out_video_full_path = out_path+out_video_name
delay = int(1000/20)
video = cv2.VideoCapture('hw3.avi')



# pre_imgs = os.listdir(path)
# pre_imgs.sort()
# print(pre_imgs)
pre_imgs = glob.glob('/Users/iijjuness/PycharmProjects/pythonProject3/lec9/images/*.bmp')
pre_imgs.sort()
img = []

for i in pre_imgs:
    i = path+i
    # print(i)
    img.append(i)

# print(img)
# print(len(img))

fourcc = cv2.VideoWriter_fourcc(*"DIVX")  # 코덱
#
frame = cv2.imread('lec9_airplane.bmp')
# size = list(frame.shape)
# # del size[2]
# # size.reverse()
# # print(size)
# #
out = cv2.VideoWriter('hw3.avi', fourcc, 20, (600, 400))  # 저장할 동영상
#
# for i in glob.glob('/Users/iijjuness/PycharmProjects/pythonProject3/lec9/images/*.bmp'):
#     img_1 = cv2.imread(i)
#     out.write(img_1)

# for i in range(len(img)-2):
#     out_1 = cv2.imread(f'{i}.bmp')
#     out.write(out_1)




while True:
    ret, frame = video.read()

    if ret == False:
        break

    str = '201715475'

    # pillow 이용하여 한글 Text 입력
    text = "이준승"
    font = ImageFont.truetype("Gwangyang_Sunshine_Bold.ttf", 30)  # font는 광양햇살 볼드체로 설정
    # font = ImageFont.load_default()
    img_pil = Image.fromarray(frame_w)  # numpy array 타입 변경
    draw = ImageDraw.Draw(img_pil)  # draw 객체 생성
    draw.text((200, 20), text, (0, 255, 255), font=font)  # 글씨 쓰기
    frame_w = np.array(img_pil)  # 다시 ndarray 형태로 변경

    cv2.putText(frame_w, str, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    for i in range(len(img) - 2):
        out_1 = cv2.imread(f'{i}.bmp')
        out.write(out_1)

out.release()
