import cv2
import os
import glob
from PIL import ImageFont, Image, ImageDraw
import numpy as np
from PIL import Image
from numpy import asarray

img1 = cv2.imread('lec9_airplane.bmp')
img2 = cv2.imread('lec9_field.bmp')


delay = int(1000/20)

# set alpha value
alpha = 0

# create an empty list to store output images
output_images = []

# loop through a range of values for alpha
for i in range(60):
    # calculate beta value
    beta = 1 - alpha

    # apply addWeighted
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)

    # append output to list
    output_images.append(output)

    # increment alpha value
    alpha += (1 / 60)


# # # print(output_images)
for j in range(20):
    output_images.insert(0, img2)
    output_images.append(img1)

fourcc = cv2.VideoWriter_fourcc(*"DIVX")  # 코덱
out = cv2.VideoWriter('hw3___000.avi', fourcc, 20, (600, 400))  # 저장할 동영상

for frame in output_images:
    out.write(frame)

out.release()
while True:




out.release()

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

