import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
import scipy.io.wavfile as wf
import numpy as np
import os

the_max = 32767
the_min = -32768
the_average = (the_max + the_min) / 2
the_range = (the_max - the_min) / 2

# Used to shuffle the contents of 
def shuffle_in_unison_scary(a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)

# Define the base directory of our project
basedir = os.path.abspath(os.path.dirname(__file__))

# Create master list
x_all = list([])
y_all = list()

# Create temp list, this is where our memmap info will be stored
temp_list = []

# List of folders in the test directory
words = os.listdir(basedir + '/dataset')

# Iterate through each directory
for word in words:

    # Grab all wav files from each directory
    all_wav = os.listdir(basedir + '/dataset/{}'.format(word))

    # Open each wav file, dump contents, and record y value
    for wav in all_wav:
        freq, data = wf.read(basedir + '/dataset/{}/'.format(word) + wav, 'rb')

        wav_counter = 0
        # Each audio clip will be 2 seconds long
        for i in range(210):
            temp_list.append([])
            for j in range(210):
                try:
                    current_num = data[wav_counter]
                    normalized_value = (current_num - the_average) / the_range
                    temp_list[i].append(normalized_value)
                except:
                    temp_list[i].append(0)
                
                wav_counter += 1
            
        # Append a deep copy of the temp list to the x_train list and clear temp_list
        x_all.append(temp_list[:])
        temp_list.clear()

        # Append the word corresponding to the wav file to the y_train list
        y_all.append(words.index(word))


# Shuffle all elements in both arrays at the same time
shuffle_in_unison_scary(x_all, y_all)

# Put in the first 90 elements from the array into training lists
x_train_arr = x_all[:150]
y_train_arr = y_all[:150]

# Put in the last 10 elements from the array into testing lists
x_test_arr = x_all[150:]
y_test_arr = y_all[150:]

# Cast these lists into numpy arrays so they play nicely with tensorflow
x_train = np.array(x_train_arr)
y_train = np.array(y_train_arr)

x_test = np.array(x_test_arr)
y_test = np.array(y_test_arr)

# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)
# print(y_test)

# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(y_train.shape)


model = Sequential()

model.add(LSTM(128, input_shape=(x_test.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(2, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)

model.compile(loss='sparse_categorical_crossentropy', 
                optimizer=opt, 
                metrics=['accuracy'])

model.fit(x_train, y_train, epochs=40, validation_data=(x_test, y_test))
