import png
import numpy as np 
from scipy.io import wavfile as wf
from scipy.misc import imsave
import math
import os
import wave

count = 0

files = os.listdir('/Users/brentredmon/Documents/School/Fall_2018/ML/Final_Project/dataset/get')
for file in files:
    print(file)
    
    try:
        audio = wave.open('/Users/brentredmon/Documents/School/Fall_2018/ML/Final_Project/dataset/get/' + file, 'rb')
        frames = audio.getnframes()
        audio_bytes = audio.readframes(frames)

        image_1D = list(audio_bytes)
        print(image_1D)

        for i in range(44100 - len(image_1D)):
            try:
                image_1D.append(0)
            except:
                continue

        image_2D = np.reshape(image_1D, (210, 210))

        imsave('test.jpg', image_2D)
        print('hi')
        count += 1
    
    except:
        print('An error occurred')