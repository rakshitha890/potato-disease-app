import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("potato_model.h5")

classes = ["Early Blight", "Late Blight", "Healthy"]

st.title("🌿 Potato Leaf Disease Detection")

uploaded_file = st.file_uploader("Upload leaf image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((224,224))
    st.image(image, caption="Uploaded Image")

    img = np.array(image)/255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    result = classes[np.argmax(prediction)]

    st.success(f"Prediction: {result}")