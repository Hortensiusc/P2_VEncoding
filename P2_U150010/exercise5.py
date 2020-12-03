# Carlos Hortensius U150010

# Practice 2  Video Encoding

import os
import subprocess

print('Welcome to Practice 2: Introduce the path where your file is located:\n')
path = input()
os.chdir(path)

print('Introduce the name of your video:')
video = input()

print('What do you want to do with your video')
print('1 -> Know some relevant information')
print('2 -> Rename the file')
print('3 -> Resize it')
print('4 -> Change the video codec')

while True:
    option = int(input("-> "))

    if option == 1:
        cmd = 'ffprobe -show_streams -select_streams v:0 %s > infovideo.txt' % video
        subprocess.call(cmd, shell=True)
        cmd = 'ffprobe -show_streams -select_streams a:0 %s > infoaudio.txt' % video
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
        print('Audio Codec: ', data)

        print('Dimensions of the video')
        print(w)
        print(h)

        break

    elif option == 2:
        print('Introduce the new name for your file:\n')
        newname = input()

        subprocess.call(['mv', video, newname])

        break

    elif option == 3:
        print('Introduce the width for your file:')
        width = int(input())
        print('Introduce the long for your file:')
        height = int(input())

        cmd = 'ffmpeg -i %s -vf scale=%d:%d resized' % (video, width, height)

        subprocess.call(cmd, shell=True)
        print('Your video with the new size has been saved as resized')

        break

    elif option == 4:
        print('Which video codec do you want?')
        print('1- MPEG4')
        print('2- h.264')
        print('3- h.265')
        print('4- AV1')
        codec_option = int(input())

        if codec_option == 1:
            subprocess.call(['ffmpeg', '-i', video, '-c:v', 'mpeg4', 'Newcodecfile'])
        if codec_option == 2:
            subprocess.call(['ffmpeg', '-i', video, '-c:v', 'libx264', 'Newcodecfil'])
        if codec_option == 3:
            subprocess.call(['ffmpeg', '-i', video, '-c:v', 'libx265', 'Newcodecfile'])
        if codec_option == 4:
            subprocess.call(['ffmpeg', '-i', video, '-c:v', 'libaom-av1', 'Newcodecfile'])

        print('Your video with the new codec has been saved as Newcodecfile')

        break

    else:
        print("Invalid option")