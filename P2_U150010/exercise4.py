# Carlos Hortensius U150010

# Practice 2  Video Encoding

import os
import subprocess


print('Welcome to Practice 2: Introduce the path where your file is located:\n')
path = input()
os.chdir(path)

print('Introduce the name of your file:')
file = input()

print('Which video codec do you want?')
print('1- MPEG4')
print('2- h264+')
print('2- MP4')
print('2- h.264')
option = int(input())

if option == 1:
    subprocess.call(['ffmpeg', '-i', file, '-c:v', 'mpeg4', 'Newcodecfile.mp4'])
if option == 1:
    subprocess.call(['ffmpeg', '-i', file, '-c:v', 'h264','Newcodecfile.mp4'])
if option == 1:
    subprocess.call(['ffmpeg', '-i', file, '-c:v', 'Newcodecfile.mp4'])
if option == 1:
    subprocess.call(['ffmpeg', '-i', file, '-c:v', 'Newcodecfile.mp4'])
    