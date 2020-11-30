# Carlos Hortensius U150010

# Practice 2  Video Encoding

import os
import subprocess


print('Welcome to Practice 2: Introduce the path where your video is located:')
path = input()
os.chdir(path)

print('Introduce the name of your video:')
video = input()

cmd = 'ffprobe -show_streams -select_streams v:0 %s > infovideo.txt' %video
subprocess.call(cmd, shell=True)
cmd = 'ffprobe -show_streams -select_streams a:0 %s > infoaudio.txt' %video
subprocess.call(cmd, shell=True)


with open("infovideo.txt") as f:
    data = f.readlines()[2]
    f.close()

with open("infovideo.txt") as f:
    w = f.readlines()[9]
    f.close()

with open("infovideo.txt") as f:
    h = f.readlines()[10]
    f.close()

print('Video Codec: ', data)

with open("infoaudio.txt") as f:
    data = f.readlines()[2]
print('Audio Codec: ',data)

print('Dimensions of the video')
print(w)
print(h)
