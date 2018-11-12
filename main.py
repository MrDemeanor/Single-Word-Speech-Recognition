import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
from IPython.display import display
from PIL import Image

train_path = 'dataset/train'
test_path = 'dataset/test'
validate_path = 'dataset/validate'

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(640, 480), classes=['are', 'get', 'has', 'is', 'know'], batch_size=10)
validate_batches = ImageDataGenerator().flow_from_directory(validate_path, target_size=(640, 480), classes=['are', 'get', 'has', 'is', 'know'], batch_size=5)
test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(640, 480), classes=['are', 'get', 'has', 'is', 'know'], batch_size=5)

imgs, labels = next(train_batches)

'''
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(640, 480, 3)),
    Flatten(),
    Dense(5, activation='softmax')
])

model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit_generator(train_batches, steps_per_epoch=6,
                    validation_data=validate_batches, validation_steps=5, epochs=5, verbose=2)
'''

vgg16_model = keras.applications.vgg16.VGG16(weights=None,classes=5,input_shape=(640,480,3))
print(vgg16_model.summary())

model = Sequential()

for layer in vgg16_model.layers:
    model.add(layer)

model.layers.pop()

for layer in model.layers:
    layer.trainable = False

model.add(Dense(5, activation='softmax'))

model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(train_batches, steps_per_epoch=6,
                    validation_data=validate_batches, validation_steps=5, epochs=5, verbose=2)
