import cv2
import numpy as np
import glob
import os

airplane = cv2.imread('lec9_airplane.bmp')
field = cv2.imread('lec9_field.bmp')


w = 600
h = 400
path = '/Users/iijjuness/PycharmProjects/pythonProject3/lec9'

img1 = cv2.addWeighted(field, 0.9, airplane, 0.1, 0)
img2 = cv2.addWeighted(field, 0.7, airplane, 0.3, 0)
img3 = cv2.addWeighted(field, 0.5, airplane, 0.5, 0)
img4 = cv2.addWeighted(field, 0.3, airplane, 0.7, 0)
img5 = cv2.addWeighted(field, 0.1, airplane, 0.9, 0)

dst1 = cv2.imwrite('1.bmp', img1)
dst2 = cv2.imwrite('2.bmp', img2)
dst3 = cv2.imwrite('3.bmp', img3)
dst4 = cv2.imwrite('4.bmp', img4)
dst5 = cv2.imwrite('5.bmp', img5)

fourcc = cv2.VideoWriter_fourcc(*"DIVX")  # 코덱
out = cv2.VideoWriter('1.avi', fourcc, 5, (w, h))  # 저장할 동영상

for filename in glob.glob('lec9/.*.bmp'):
    img = cv2.imread(filename)
    out.write(img)


out.release()

cv2.imshow('0', field)
cv2.imshow('1', img1)
cv2.imshow('2', img2)
cv2.imshow('3', img3)
cv2.imshow('4', img4)
cv2.imshow('5', img5)
cv2.imshow('6', airplane)
cv2.waitKey(0)






# # print(pre_img)
# img = []
#
# for i in pre_img:
#     i = path + i
#     # print(i)
#     img.append(i)
#
# print(img)
#
# fourcc = cv2.VideoWriter_fourcc(*"DIVX")
# out = cv2.VideoWriter('window.avi', fourcc, 20, (w, h))
#
#
# for i in range(len(img)):
#     out.write(img[i])
#
# out.release()


# img = []
# for i in pre_img:
#     i = path + i
#     # print(i)
#     img.append(i)
# img_array = []
# for i in glob.glob('/Users/iijjuness/PycharmProjects/pythonProject3/lec9\*.bmp'):
#     img = cv2.imread(i)
#     h, w, c = img.shape
#     size = (w, h)
#     img_array.append(img)
#
# print(img_array)
#
# fourcc = cv2.VideoWriter_fourcc(*"DIVX")
#
# frame = cv2.imread(img[0])
#
# out = cv2.VideoWriter('window.avi', fourcc, 20, size_1)

# for i in range(len(img)):
#     out.write(img[i])
#     print('frame ', i + 1, ' of ', len(img))

# cv2.imshow('window', img[:])
# cv2.waitKey(0)
# out.release()


