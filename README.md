# HandWritten Digit Recognition

**A Python-based project that recognizes handwritten digits (0–9) using machine learning / deep learning techniques. This project includes training a model on the MNIST dataset and building a simple app to make predictions.**

Built as a submission for **Turing's Playground WOC 9**

Github Repository → [https://github.com/ankurmehtax2007-stack/HandWritten-Digit-Recogniton/tree/main](https://github.com/ankurmehtax2007-stack/HandWritten-Digit-Recogniton/tree/main)
## Dataset
The MNIST dataset is a classic benchmark in machine learning for digit recognition and contains 70,000 grayscale images (60,000 for training and 10,000 for testing).

## 🚀 Features

- 📥 Load and preprocess the MNIST dataset  
- 🧠 Train a digit recognition model  
- 🔍 Predict digits from new images  
- 🖼️ Simple app for digit input and prediction  

---

## 🧠 How It Works

The system uses a neural network (e.g., TensorFlow/Keras) to learn patterns from thousands of handwritten digit images. After training, the model can recognize and classify new digit images provided by the user. :contentReference[oaicite:2]{index=2}

---

## 🛠️ Requirements

Before you begin, make sure you have:

- **Python 3.7 or later**  
- **pip**

Install all required packages with:

```bash
pip install -r requirements.txt
```


## Getting Started
**1. Train the Model**

Run the training script:
```bash
python train.py
```
This will train the model and (optionally) save it for later use.
The script will output the predicted digit.

**2. Run the App**

Launch the app interface (e.g., for drawing or uploading digits):
```bash
streamlit run app.py
```
## Example Output
![WhatsApp Image 2026-01-23 at 9 05 24 PM](https://github.com/user-attachments/assets/8036a904-e667-4f4b-87e6-c50c3eba7bab)

## 🔮 Future Plans
- Handwritten alphabet recognition
- Multi-digit recognition
- Stroke smoothing
- Save prediction history

