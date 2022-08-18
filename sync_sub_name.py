import glob
import os
import time


print("Enter root path")
root_path = input() + '/'
root_path = root_path.replace(os.sep, '/')

print("root_path: " + root_path)

types = ('*.avi', '*.mp4', '*.wmv', '*.mkv', '*.webm', '*.mpg')
video = []

for files in types:
    video.extend(glob.glob(root_path + files))

video.sort()

# convert to names only
video = [os.path.splitext(x)[0] for x in video]

# SRT

srt_path = root_path + "/*.srt"

srt = glob.glob(srt_path)

srt.sort()

# convert to names only
#srt = [os.path.splitext(x)[0] for x in srt]


if len(video) == len(srt):
    for i in range(len(video)):
        os.rename(srt[i], video[i] + ".srt")
        print("old name: " + srt[i] + " new name: " + video[i] + ".srt \n")
else:
    print("Number of videos detected: " + str(len(video)) + \
          "\nNumber of SRT detected: " + str(len(srt)))
