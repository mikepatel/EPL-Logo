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
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import tensorflow as tf

from parameters import *
from model import build_cnn


################################################################################
# get class labels
# return: labels, number of labels
def get_labels():
    labels = []
    int2club = {}
    directories = os.listdir(os.path.join(os.getcwd(), "data\\Train"))
    for i in range(len(directories)):
        name = directories[i]
        labels.append(name)
        int2club[i] = name

    num_labels = len(labels)

    return labels, num_labels, int2club


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
    classes, num_classes, int2class = get_labels()
    print(f'Number of classes (aka clubs): {num_classes}')

    # training
    # build image generators
    image_generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=90,  # degrees
        width_shift_range=1.0,  # interval [-1.0, 1.0)
        height_shift_range=1.0,  # interval [-1.0, 1.0)
        brightness_range=[0.0, 1.0],  # 0 no brightness, 1 max brightness
        shear_range=30,  # stretching in degrees
        zoom_range=[0.5, 1.5],  # less than 1.0 zoom in, more than 1.0 zoom out
        zca_whitening=True,
        #channel_shift_range,
        horizontal_flip=True,
        vertical_flip=True,
        rescale=1./255  # [0, 255] --> [0, 1]
    )

    # apply image generators
    train_data_gen = image_generator.flow_from_directory(
        directory=os.path.join(os.getcwd(), "data\\Train"),
        target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
        class_mode="sparse",  # more than 2 classes
        classes=classes,
        batch_size=BATCH_SIZE,
        shuffle=True
        #save_to_dir=os.path.join(os.getcwd(), "data\\x")  # temporary for visualising
    )

    #next(train_data_gen)

    # validation
    val_data_gen = image_generator.flow_from_directory(
        directory=os.path.join(os.getcwd(), "data\\Validation"),
        target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
        class_mode="sparse",  # more than 2 classes
        classes=classes,
        batch_size=BATCH_SIZE,
        shuffle=True
    )

    # test

    # ----- MODEL ----- #
    m = build_cnn(num_classes=num_classes)
    m.compile(
        loss=tf.keras.losses.sparse_categorical_crossentropy,
        optimizer=tf.keras.optimizers.Adam(),
        metrics=["accuracy"]
    )

    m.summary()

    # ----- TRAINING ----- #
    history = m.fit(
        x=train_data_gen,
        epochs=NUM_EPOCHS,
        validation_data=val_data_gen
    )

    # plot accuracy
    plt.plot(history.history["accuracy"], label="accuracy")
    plt.plot(history.history["val_accuracy"], label="val_accuracy")
    plt.title("Training Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.ylim([0.0, 1.1])
    plt.grid()
    plt.legend(loc="lower right")
    plt.savefig(os.path.join(output_dir, "Training Accuracy"))

    # save model
    m.save(os.path.join(output_dir, "saved_model"))

    # ----- GENERATE ----- #
    test_images = [
        "burnley-fc\\burnley-fc.jpg",
        "charlton-athletic-fc\\charlton-athletic-fc.jpg",
        "wolverhampton-wanderers-fc\\wolverhampton-wanderers-fc.jpg",
        "crystal-palace-fc\\crystal-palace-fc.jpg",
        "nottingham-forest-fc\\nottingham-forest-fc.jpg"
    ]

    for ti in test_images:
        test_image_path = os.path.join(os.getcwd(), "data\\Test\\" + ti)
        test_image = Image.open(test_image_path)
        test_image = test_image.convert("RGB")

        test_image = np.array(test_image).astype(np.float32) / 255.0
        test_image = np.expand_dims(test_image, 0)

        prediction = m.predict(test_image)
        print(f'Prediction: {int2class[int(np.argmax(prediction))].title()}')
