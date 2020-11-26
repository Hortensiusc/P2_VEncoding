# Carlos Hortensius U150010

# Practice 2  Video Encoding

import os
import subprocess


print('Welcome to Practice 2: Introduce the path where your file is located:\n')
path = input()
os.chdir(path)

print('Introduce the name of your file:')
file = input()

print('Introduce the width for your file:')
width = int(input())
print('Introduce the long for your file:')
height = int(input())

print('Are you resizing a video or just an image?')
print('1- Video')
print('2- Image')
option = int(input())

if option == 1:
    cmd = 'ffmpeg -i %s -vf scale=%d:%d resized.mp4' % (file, width, height)
if option == 2:
    cmd = 'ffmpeg -i %s -vf scale=%d:%d resized.png' % (file, width, height)

print(cmd)

subprocess.call(cmd, shell=True)




