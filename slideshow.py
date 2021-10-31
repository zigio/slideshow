#! /usr/bin/python3
import os
import cv2
import argparse
import moviepy.editor as mpe

# parse arguments
parser = argparse.ArgumentParser(description='Create slideshow from images')
parser.add_argument('-i', '--input_directory', help='set input dir with images', default='~/Pictures')
parser.add_argument('-o', '--output_directory', help='set output directory for video', default='~/Videos')
parser.add_argument('-n', '--name', help='set video name', default='video.mp4')
parser.add_argument('-s', '--size', help='set video size, example: 960x720', default='960x720')
parser.add_argument('-f', '--fps', help='set how many pictures should be present in one frame', default='0.15')
parser.add_argument('-a', '--audio', help='add audio to background', default=None)

args = parser.parse_args()

os.chdir(args.input_directory)
dir_path = os.getcwd()

width, height = args.size.split('x')

jpg = '.jpg'
png = '.png'
output = args.name
shape = int(width), int(height)
fps = float(args.fps)

# get images list
images = [f for f in os.listdir(dir_path) if f.endswith(jpg) or f.endswith(png)]

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

os.chdir(args.output_directory)
video = cv2.VideoWriter(output, fourcc, fps, shape)

# resize image and add to video
for image in images:
    image_path = os.path.join(dir_path, image)
    image = cv2.imread(image_path)
    resized=cv2.resize(image,shape)
    video.write(resized)

video.release()

if args.audio is not None:
    vid = args.output_directory + args.name
    audio = mpe.AudioFileClip(args.audio)
    clip = mpe.VideoFileClip(vid)
    loop = mpe.afx.audio_loop(audio, duration=clip.duration)
    final_clip = clip.set_audio(loop)
    os.remove(vid)
    final_clip.write_videofile(args.name)
