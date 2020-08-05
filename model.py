"""
Michael Patel
June 2020

Project description:
    CNN for EPL logos

File description:
    For model definitions
"""
################################################################################
# Import
from parameters import *


################################################################################
# CNN
def build_cnn(num_classes):
    model = tf.keras.Sequential()

    # Convolution 1
    model.add(tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS),
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Convolution 2
    model.add(tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=(3, 3),
        strides=2,
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Convolution 3
    model.add(tf.keras.layers.Conv2D(
        filters=128,
        kernel_size=(3, 3),
        strides=2,
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Convolution 4
    model.add(tf.keras.layers.Conv2D(
        filters=256,
        kernel_size=(3, 3),
        strides=2,
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Flatten
    model.add(tf.keras.layers.Flatten())

    # Fully Connected
    model.add(tf.keras.layers.Dense(
        units=256,
        activation=tf.keras.activations.relu
    ))

    # Output
    model.add(tf.keras.layers.Dense(
        units=num_classes,
        activation=tf.keras.activations.softmax
    ))

    return model
