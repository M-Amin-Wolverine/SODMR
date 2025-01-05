import streamlit as st
import numpy as np
import os
import cv2

# Cache the function to load images, suppress spinner display
@st.cache(show_spinner=False)
def load_image_data():
    # Load the training data from the specified file
    training_data = np.load("training_data/training_data-0.npy", allow_pickle=True)
    return training_data

# Sidebar title and slider
st.sidebar.title("GTAV Dataset Viewer")
images = load_image_data()
frame_id = st.sidebar.slider("Select Frame", 0, len(images) - 1, 0)

# Display the recorded time for the selected frame
st.sidebar.markdown("## Recorded Time:")
st.sidebar.write(images[frame_id][1])

# Display the selected frame image
st.image(images[frame_id][0], width=600, caption=f"Frame {frame_id}")
