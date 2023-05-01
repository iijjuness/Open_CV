import cv2
import os

frame_size = (600, 400)
fps = 30

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_filename = 'output.avi'
video_writer = cv2.VideoWriter(video_filename, fourcc, fps, frame_size)

image_folder = '/Users/iijjuness/PycharmProjects/pythonProject3/lec9'
images = os.listdir(image_folder)
images.sort()

for image_filename in images:
    image_path = os.path.join(image_folder, image_filename)
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, frame_size)
    video_writer.write(resized_image)

video_writer.release()
