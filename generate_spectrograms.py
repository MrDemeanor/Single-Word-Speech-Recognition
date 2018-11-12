import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import os

directory = 'dataset/validate/know/'

files = os.listdir(directory)

file_number = 0

for file in files:

    sample_rate, samples = wavfile.read(directory + file)

    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.pcolormesh(times, frequencies, spectrogram)

    plt.savefig(directory + str(file_number) + '.png')

    file_number += 1
