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

import tensorflow as tf

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

    # number of classes = number of clubs

    # ----- MODEL ----- #

    # ----- TRAINING ----- #
