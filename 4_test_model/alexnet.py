# alexnet.py

""" AlexNet.
Applying 'AlexNet' to Oxford's 17 Category Flower Dataset classification task.
References:
    - Alex Krizhevsky, Ilya Sutskever and Geoffrey E. Hinton. ImageNet
    Classification with Deep Convolutional Neural Networks. NIPS, 2012.

Links:
    - [AlexNet Paper](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
"""

import tensorflow as tf
from tensorflow.keras import layers, models

def alexnet(width, height, learning_rate):
    model = models.Sequential()

    model.add(layers.Conv2D(96, kernel_size=(11, 11), strides=(4, 4), activation='relu', input_shape=(width, height, 3)))
    model.add(layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
    model.add(layers.BatchNormalization())
    
    model.add(layers.Conv2D(256, kernel_size=(5, 5), activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
    model.add(layers.BatchNormalization())
    
    model.add(layers.Conv2D(384, kernel_size=(3, 3), activation='relu'))
    model.add(layers.Conv2D(384, kernel_size=(3, 3), activation='relu'))
    model.add(layers.Conv2D(256, kernel_size=(3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
    model.add(layers.BatchNormalization())
    
    model.add(layers.Flatten())
    model.add(layers.Dense(4096, activation='tanh'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(4096, activation='tanh'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(17, activation='softmax'))  # Assuming 17 categories

    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate, momentum=0.9),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model

# Example of how to create the model
# model = alexnet(224, 224, 0.001)
