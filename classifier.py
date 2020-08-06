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
from parameters import *


################################################################################
# Main
if __name__ == "__main__":
    # data labels
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

    # load trained model
    model = tf.keras.models.load_model(SAVE_DIR)
    model.summary()

    """
    t = os.path.join(TRAIN_DIR, "liverpool-fc\\liverpool-fc.jpg")
    #t = os.path.join(os.getcwd(), "cv.jpg")
    
    image = Image.open(t)
    image = image.convert("RGB")
    image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    image = np.array(image)
    image = image.reshape(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)
    image = image / 255.0
    image = np.expand_dims(image, 0)

    x = model.predict(image)
    x = int(np.argmax(x))
    x = int2class[x]
    print(x)

    quit()
    """

    # open webcam
    capture = cv2.VideoCapture(0)
    while True:
        # capture frame by frame
        ret, frame = capture.read()

        # preprocess image
        image = frame

        # crop webcam image
        y, x, channels = image.shape
        left_x = int(x*0.25)
        right_x = int(x*0.75)
        top_y = int(y*0.25)
        bottom_y = int(y*0.75)
        image = image[top_y:bottom_y, left_x:right_x]

        predicted_image_filepath = os.path.join(os.getcwd(), "predicted.jpg")
        cv2.imwrite(predicted_image_filepath, image)

        # convert to RGB
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # resize image
        image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))

        mod_image = image

        # array and rescale
        image = np.array(image)
        image = image / 255.0
        image = np.expand_dims(image, 0)

        # make prediction
        prediction = model.predict(image)
        prediction = int(np.argmax(prediction))
        prediction = int2class[prediction]
        print(prediction)

        # display frame
        #cv2.imshow("", frame)
        cv2.imshow("", mod_image)

        # label webcam image with predicted label
        webcam_frame_image = Image.open(predicted_image_filepath)
        draw = ImageDraw.Draw(webcam_frame_image)
        font = ImageFont.truetype("arial.ttf", 40)
        draw.text((0, 0), prediction, font=font)
        webcam_frame_image.save(predicted_image_filepath)

        # continuous stream, escape key
        if cv2.waitKey(1) == 27:
            break

    # release capture
    capture.release()
    cv2.destroyAllWindows()
