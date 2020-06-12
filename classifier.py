"""
Michael Patel
June 2020

Project description:
    CNN for EPL logos

File description:
    For running trained model
"""
################################################################################
# Import
import os
import numpy as np
from PIL import Image
import cv2

import tensorflow as tf

from parameters import *


################################################################################
# Main
if __name__ == "__main__":
    # create mapping of integers to club names
    directories = os.listdir(os.path.join(os.getcwd(), "data\\Train"))
    int2club = {}
    for i in range(len(directories)):
        name = directories[i]
        int2club[i] = name

    # load model
    model_filepath = os.path.join(os.getcwd(), "results\\saved_model")
    model = tf.keras.models.load_model(model_filepath)

    # use webcam to get image, then classify
    # open webcam and capture video
    capture = cv2.VideoCapture(0)  # 0 = first camera

    while True:
        # capture frame by frame
        ret, frame = capture.read()

        # preprocess image
        image = frame
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
        Image.fromarray(image).save(os.path.join(os.getcwd(), "results\\t.png"))

        #image = np.array(image).astype(np.float32) / 255.0
        image = np.array(image).astype(np.float)
        image = np.expand_dims(image, 0)

        # make prediction
        prediction = model.predict(image)
        print(int2club[int(np.argmax(prediction))])

        # display resulting frame
        cv2.imshow("", frame)

        if cv2.waitKey(1) == 27:  # continuous stream, escape key
            break

    # release capture
    capture.release()
    cv2.destroyAllWindows()
