# Carlos Hortensius U150010

# Practice 2  Video Encoding

import os
import subprocess


print('Welcome to Practice 2: Introduce the path where your video is located:\n')
path = input()
os.chdir(path)

print('Introduce the name of your video:\n')
video = input()

subprocess.call(['ffprobe', '-show_streams', '-select_streams', 'v:0', video, '>', 'infovideo.txt'])
subprocess.call(['ffprobe', '-show_streams', '-select_streams', 'a:0', video, '>', 'infoaudio.txt'])
subprocess.call(['ffprobe', '-show_streams', '-select_streams', 'a:1', video, '>', 'infoaudio2.txt'])

