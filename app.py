from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import base64, io

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model("model.h5")

def preprocess(img_b64):
    img_b64 = img_b64.split(",")[1]
    img = Image.open(io.BytesIO(base64.b64decode(img_b64))).convert("L")
    img = img.resize((28, 28))
    img = np.array(img) / 255.0
    img = img.reshape(1, 28, 28, 1)
    return img

@app.route("/api/recognize", methods=["POST"])
def recognize():
    image = preprocess(request.json["image"])
    pred = model.predict(image)
    return jsonify({
        "digit": int(np.argmax(pred)),
        "confidence": float(np.max(pred))
    })

if __name__ == "__main__":
    app.run()
