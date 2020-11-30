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
print('2- h.264')
print('3- h.265')
print('4- AV1')
option = int(input())

if option == 1:
    subprocess.call(['ffmpeg', '-i', file, '-c:v', 'mpeg4', 'Newcodecfile.mp4'])
if option == 2:
    subprocess.call(['ffmpeg', '-i', file, '-c:v', 'libx264','Newcodecfil.mp4'])
if option == 3:
    subprocess.call(['ffmpeg', '-i', file, '-c:v', 'libx265', 'Newcodecfile.mp4'])
if option == 4:
    subprocess.call(['ffmpeg', '-i', file, '-c:v', 'libaom-av1',  'Newcodecfile.mp4'])
    