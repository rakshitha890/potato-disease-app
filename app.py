import streamlit as st
from PIL import Image
import numpy as np
import random

# Title
st.title("🥔 Potato Disease Detection App")

# Upload image
uploaded_file = st.file_uploader("Upload a potato leaf image", type=["jpg", "png", "jpeg"])

# Dummy prediction function (no TensorFlow)
def predict(image):
    classes = ["Early Blight", "Late Blight", "Healthy"]
    return random.choice(classes)

# If image uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Predict button
    if st.button("Predict"):
        result = predict(image)
        st.success(f"Prediction: {result}")
