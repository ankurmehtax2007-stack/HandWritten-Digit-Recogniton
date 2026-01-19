import streamlit as st
from streamlit_drawable_canvas import st_canvas
from predict import predict_digit

# Page setup
st.set_page_config(page_title="Digit Recognizer")
st.title("Handwritten Digit Recognizer")
st.markdown("Draw a digit (0-9) in the box below!")

# Drawing canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=20,
    stroke_color="#FFFFFF",
    background_color="#000000",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

# Predict button
if canvas_result.image_data is not None:
    if st.button("Recognize"):
        digit, confidence = predict_digit(canvas_result.image_data)

        if digit is None:
            st.error("Model file 'digit_model.h5' not found.")
        else:
            st.write(f"## Prediction: {digit}")
            st.write(f"Confidence: {confidence:.2%}")
            st.progress(confidence)

# Sidebar
st.sidebar.header("Instructions")
st.sidebar.info(
    "1. Draw a single digit in the center.\n"
    "2. Click 'Recognize' to see the AI's guess.\n"
    "3. Use the undo/clear tools below the canvas to reset."
)
