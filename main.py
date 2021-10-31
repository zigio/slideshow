#! /usr/bin/python3
import os
import cv2

os.chdir("images")
dir_path = os.getcwd()

ext = '.jpg'
output = 'video.avi'
shape = 960, 720
fps = 1

images = [f for f in os.listdir(dir_path) if f.endswith(ext)]

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(output, fourcc, fps, shape)

for image in images:
    image_path = os.path.join(dir_path, image)
    image = cv2.imread(image_path)
    resized=cv2.resize(image,shape)
    video.write(resized)

video.release()
