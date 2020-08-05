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
from parameters import *
from model import build_cnn


################################################################################
# Main
if __name__ == "__main__":
    # print TF version
    print(f'TF version: {tf.__version__}')

    # ----- ETL ----- #
    # ETL = Extraction, Transformation, Load
    # labels
    classes = []
    int2class = {}
    directories = os.listdir(TRAIN_DIR)
    for i in range(len(directories)):
        name = directories[i]
        classes.append(name)
        int2class[i] = name

    num_classes = len(classes)

    print(f'Classes: {classes}')
    print(f'Number of classes: {num_classes}')

    # image generator
    image_generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=30,  # degrees
        width_shift_range=0.3,  # interval [-1.0, 1.0]
        height_shift_range=0.3,  # interval [-1.0, 1.0]
        brightness_range=[0.3, 1.0],  # 0 is no brightness, 1 is max brightness
        zoom_range=[0.7, 1.3],  # less than 1.0 is zoom in, more than 1.0 is zoom out
        rescale=1./255  # [0, 255] --> [0, 1]
    )

    # train generator
    train_data_gen = image_generator.flow_from_directory(
        directory=TRAIN_DIR,
        target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
        class_mode="categorical",
        batch_size=BATCH_SIZE,
        shuffle=True
        #save_to_dir=TEMP_DIR
    )

    # validation generator
    val_data_gen = image_generator.flow_from_directory(
        directory=VAL_DIR,
        target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
        class_mode="categorical",
        batch_size=BATCH_SIZE,
        shuffle=True
    )

    #next(train_data_gen)
    #quit()

    # ----- MODEL ----- #
    # build model
    model = build_cnn(num_classes=num_classes)

    # loss function, optimizer
    model.compile(
        loss=tf.keras.losses.categorical_crossentropy,
        optimizer=tf.keras.optimizers.Adam(),
        metrics=["accuracy"]
    )

    model.summary()

    # ----- TRAIN ----- #
    # fit model
    history = model.fit(
        x=train_data_gen,
        epochs=NUM_EPOCHS,
        steps_per_epoch=num_classes // BATCH_SIZE,  # 1 image per class
        validation_data=val_data_gen,
        validation_steps=num_classes // BATCH_SIZE  # 1 image per class
    )

    # save model
    model.save(SAVE_DIR)

    # plot accuracy
    plt.scatter(range(1, NUM_EPOCHS + 1), history.history["accuracy"], label="accuracy", s=300)
    plt.scatter(range(1, NUM_EPOCHS + 1), history.history["val_accuracy"], label="val_accuracy", s=300)
    plt.title("Training Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.grid()
    plt.legend(loc="lower right")
    plt.savefig(os.path.join(os.getcwd(), "training"))
