import streamlit as st  
import numpy as np  
import os  
import cv2  

@st.cache_data(show_spinner=False)  # Updated to use cache_data for caching purposes  
def load_image(dataset_id):  
    try:  
        # Attempt to load the training data from the specified path  
        training_data = np.load(f"training_data/training_data-{dataset_id}.npy", allow_pickle=True)  
        return training_data  
    except FileNotFoundError:  
        st.error(f"Dataset {dataset_id} not found. Please ensure the file exists.")  
        return None  
    except Exception as e:  
        st.error(f"An error occurred while loading the dataset: {e}")  
        return None  

st.sidebar.title("GTAV Dataset")  
dataset = st.sidebar.number_input("Select Dataset", min_value=1, max_value=25, value=1, step=1)  

images = load_image(dataset)  

if images is not None:  
    id = st.sidebar.slider("Select Frame", min_value=0, max_value=len(images)-1, value=0)  

    st.sidebar.markdown("## Controller Input:")  
    st.sidebar.write(images[id][1])   

    st.title("Simulated Road Data")  
    
    # Display the selected image with appropriate width  
    st.image(images[id][0], width=600, use_column_width='auto')  

    # Uncomment the following lines if you want to display a video file  
    # video_file = open('project.mp4', 'rb')  
    # video_bytes = video_file.read()  
    # st.video(video_bytes)  
else:  
    st.warning("Please select a valid dataset.")  # Display a warning if no images were loaded
