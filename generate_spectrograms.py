import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import os

directory = 'dataset/delete/'
save = 'dataset/delete_png'
files = os.listdir(directory)

file_number = 0

for file in files:

    sample_rate, samples = wavfile.read(directory + file)

    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.pcolormesh(times, frequencies, spectrogram)

    plt.savefig(save + str(file_number) + '.png')

    file_number += 1

# # import the pyplot and wavfile modules

# import matplotlib.pyplot as plot

# from scipy.io import wavfile

# # Read the wav file (mono)

# samplingFrequency, signalData = wavfile.read('punk.wav')

# # Plot the signal read from wav file

# fig,ax = plot.subplots(1)
# fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
# ax.axis('tight')
# ax.axis('off')

# plot.specgram(signalData, Fs=samplingFrequency)

# rate, data = wavfile.read('punk.wav')
# fig,ax = plot.subplots(1)
# fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
# ax.axis('off')
# pxx, freqs, bins, im = ax.specgram(x=data, Fs=rate, noverlap=384, NFFT=512)
# ax.axis('off')

# plot.show()