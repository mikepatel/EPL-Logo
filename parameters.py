"""
Michael Patel
June 2020

Project description:
    CNN for EPL logos

File description:
    For model parameters
"""
################################################################################
# Imports
import os
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import tensorflow as tf


################################################################################
# images are 160x160
# 80x80
# 40x40
# 20x20
# 10x10
# 5x5
IMAGE_WIDTH = 160
IMAGE_HEIGHT = 160
IMAGE_CHANNELS = 3

NUM_EPOCHS = 20
BATCH_SIZE = 64
LEARNING_RATE = 0.0001

DATA_DIR = os.path.join(os.getcwd(), "data")
DATASETS_DIR = os.path.join(DATA_DIR, "datasets")
TRAIN_DIR = os.path.join(DATASETS_DIR, "Train")
TEST_DIR = os.path.join(DATASETS_DIR, "Test")
VAL_DIR = os.path.join(DATASETS_DIR, "Validation")

SAVE_DIR = os.path.join(os.getcwd(), "saved_model")

TEMP_DIR = os.path.join(os.getcwd(), "temp")
