import png
import numpy as np 
from scipy.io import wavfile as wf
from scipy.misc import imsave
import math
import os
import wave

count = 0

files = os.listdir('dataset/thing')
for file in files:
    print(file)
    
    try:
        audio = wave.open('dataset/thing/' + file, 'rb')
        frames = audio.getnframes()
        audio_bytes = audio.readframes(frames)

        image_1D = list(audio_bytes)

        for i in range(44100 - len(image_1D)):
            try:
                image_1D.append(0)
            except:
                continue

        image_2D = np.reshape(image_1D, (210, 210))

        imsave('dataset/thing_png/' + str(count) + '.png', image_2D)
        
        count += 1
    
    except:
        print('An error occurred')