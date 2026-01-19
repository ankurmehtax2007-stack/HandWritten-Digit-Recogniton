import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model (cached when imported)
@tf.keras.utils.register_keras_serializable()
def load_model():
    try:
        return tf.keras.models.load_model("digit_model.h5")
    except:
        return None

model = load_model()


def predict_digit(canvas_image_data):
    """
    Takes canvas image data from Streamlit and returns digit & confidence
    """

    if model is None:
        return None, None

    # Convert RGBA canvas image to grayscale and resize
    img = Image.fromarray(canvas_image_data.astype("uint8"), "RGBA")
    img = img.convert("L").resize((28, 28))

    # Normalize and reshape
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28)

    # Predict
    prediction = model.predict(img_array, verbose=0)
    digit = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    return digit, confidence
