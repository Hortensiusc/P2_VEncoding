#Carlos Hortensius


# Carlos Hortensius U150010

# Practice 2  Video Encoding

import os
import subprocess


print('Welcome to Practice 2: Introduce the path where your file is located:\n')
path = input()
os.chdir(path)

print('Introduce the name of your file:\n')
file = input()

print('Introduce the new name for your file:\n')
newname = input()

subprocess.call(['mv', file, newname])
