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

import tensorflow as tf

from parameters import *

################################################################################
# Main
if __name__ == "__main__":
    # load model
    model_filepath = os.path.join(os.getcwd(), "results\\saved_model")
    model = tf.keras.models.load_model(model_filepath)

    # use webcam to get image, then classify
