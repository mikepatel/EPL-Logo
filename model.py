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
import tensorflow as tf

from parameters import *


################################################################################
# CNN
def build_cnn(num_classes):
    model = tf.keras.Sequential()

    # ----- Stage 1 ----- #
    # Convolution
    model.add(tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=[3, 3],
        input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS),
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Convolution
    model.add(tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=[3, 3],
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Max Pooling
    model.add(tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2
    ))

    # Dropout
    model.add(tf.keras.layers.Dropout(
        rate=0.2
    ))

    # ----- Stage 2 ----- #
    # Convolution
    model.add(tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=[3, 3],
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Convolution
    model.add(tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=[3, 3],
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Max Pooling
    model.add(tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2
    ))

    # Dropout
    model.add(tf.keras.layers.Dropout(
        rate=0.2
    ))

    # ----- Stage 3 ----- #
    # Convolution
    model.add(tf.keras.layers.Conv2D(
        filters=128,
        kernel_size=[3, 3],
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Convolution
    model.add(tf.keras.layers.Conv2D(
        filters=128,
        kernel_size=[3, 3],
        padding="same",
        activation=tf.keras.activations.relu
    ))

    # Max Pooling
    model.add(tf.keras.layers.MaxPool2D(
        pool_size=[2, 2],
        strides=2
    ))

    # Dropout
    model.add(tf.keras.layers.Dropout(
        rate=0.2
    ))

    # ----- Stage 4 ----- #
    # Flatten
    model.add(tf.keras.layers.Flatten())

    # Dense
    model.add(tf.keras.layers.Dense(
        units=256,
        activation=tf.keras.activations.relu
    ))

    # Dropout
    model.add(tf.keras.layers.Dropout(
        rate=0.5
    ))

    # Dense - output
    model.add(tf.keras.layers.Dense(
        units=num_classes,
        activation=tf.keras.activations.softmax
    ))

    return model
