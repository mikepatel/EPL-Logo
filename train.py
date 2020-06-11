"""
Michael Patel
June 2020

Project description:
    CNN for EPL logos

File description:
    For preprocessing and training
"""
################################################################################
# Import
import os
from datetime import datetime
import matplotlib.pyplot as plt

import tensorflow as tf

from parameters import *


################################################################################
# get class labels
# return: labels, number of labels
def get_labels():
    labels = []
    for directories in os.listdir(os.path.join(os.getcwd(), "data\\Train")):
        labels.append(directories)

    num_labels = len(labels)

    return labels, num_labels


# plot images in a 1x5 grid
def plot_images(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


################################################################################
# Main
if __name__ == "__main__":
    # print TF version
    print(f'TF version: {tf.__version__}')

    # create output directory for results
    output_dir = "results\\" + datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # ----- ETL ----- #
    # ETL = Extraction, Transformation, Load
    # use ImageDataGenerator to augment dataset

    # get class labels
    # number of classes = number of clubs
    classes, num_classes = get_labels()
    print(f'Number of classes (aka clubs): {num_classes}')

    ## training
    # build image generators
    train_image_generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=30,  # degrees
        width_shift_range=1.0,  # interval [-1.0, 1.0)
        height_shift_range=1.0,  # interval [-1.0, 1.0)
        brightness_range=[0.0, 1.0],  # 0 no brightness, 1 max brightness
        shear_range=30,  # stretching in degrees
        zoom_range=[0.5, 1.5],  # less than 1.0 zoom in, more than 1.0 zoom out
        #channel_shift_range,
        horizontal_flip=True,
        vertical_flip=True,
        rescale=1./255  # [0, 255] --> [0, 1]
    )

    # apply image generators
    train_data_gen = train_image_generator.flow_from_directory(
        directory=os.path.join(os.getcwd(), "data\\Train"),
        target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
        class_mode="categorical",  # more than 2 classes
        classes=classes,
        batch_size=BATCH_SIZE,
        shuffle=True
        #save_to_dir=os.path.join(os.getcwd(), "data\\x")  # temporary for visualising
    )

    #next(train_data_gen)

    ## validation
    val_image_generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255
    )

    val_data_gen = val_image_generator.flow_from_directory(
        directory=os.path.join(os.getcwd(), "data\\Validation"),
        target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
        class_mode="categorical",  # more than 2 classes
        classes=classes,
        batch_size=BATCH_SIZE,
        shuffle=True
    )

    ## test



    # ----- MODEL ----- #

    # ----- TRAINING ----- #
