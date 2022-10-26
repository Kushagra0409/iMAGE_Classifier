from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
from tensorflow import keras
from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent

_model = keras.models.load_model(f"{BASE_DIR}/test1.h5")

def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image


class_names=['Bag','Bat','Bathtub','Binocular','Cactus','Calculator','Chopsticks','Computer Keyboard','Computer Monitor','Computer Mouse','Insect','Mug','Radio']


def predict(image: Image.Image):
    image = np.asarray(image.resize((256, 256)))[..., :3]
    img_array1 = np.expand_dims(image, 0)

    predictions = _model.predict(img_array1)
    score = tf.nn.softmax(predictions[0])
    str = "This image most likely belongs to {}.".format(class_names[np.argmax(score)])
    
    return str