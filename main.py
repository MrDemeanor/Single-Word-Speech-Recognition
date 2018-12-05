import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
import scipy.io.wavfile as wf
import numpy as np
import os
from PIL import Image
import random

# Define the base directory of our project
basedir = os.path.abspath(os.path.dirname(__file__))

# Create temp list, this is where our memmap info will be stored
temp_list = []

# List of folders in the test directory
words = os.listdir(basedir + '/dataset/have_png')

for word in words:
    img = Image.open('dataset/have_png/' + word)
    my_list = list(img.getdata())
    my_list_reshaped = np.reshape(my_list, (210, 210))
    temp_list.append(tuple((my_list_reshaped, 0)))

# List of folders in the test directory
words = os.listdir(basedir + '/dataset/thing_png')

for word in words:
    img = Image.open('dataset/thing_png/' + word)
    my_list = list(img.getdata())
    my_list_reshaped = np.reshape(my_list, (210, 210))
    temp_list.append(tuple((my_list_reshaped, 1)))

random.shuffle(temp_list)

temp_array = np.array(temp_list)

x_train_list = list()
x_test_list = list()
y_train_list = list()
y_test_list = list()

for i in range(180):
    x_train_list.append(temp_list[i][0])

for i in range(180):
    y_train_list.append(temp_list[i][1])

for i in range(180, temp_list.__len__()):
    x_test_list.append(temp_list[i][0])

for i in range(180, temp_list.__len__()):
    y_test_list.append(temp_list[i][1])

x_train = np.array(x_train_list)
y_train = np.array(y_train_list)
x_test = np.array(x_test_list)
y_test = np.array(y_test_list)

x_train = x_train / 255
x_test = x_test / 255

print('x_train shape: {}'.format(x_train.shape))
print('y_train shape: {}'.format(y_train.shape))
print('x_test shape: {}'.format(x_test.shape))
print('y_test shape: {}'.format(y_test.shape))


model = Sequential()

model.add(LSTM(128, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(2, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=1e-5, decay=1e-4)

model.compile(loss='sparse_categorical_crossentropy', 
                optimizer=opt, 
                metrics=['accuracy'])

model.fit(x_train, y_train, epochs=40, validation_data=(x_test, y_test))
