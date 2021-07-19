import streamlit as st
import numpy as np
import cv2 as cv
import mediapipe as mp
from PIL import Image
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
model_face_mesh = mp_face_mesh.FaceMesh()
st.title("OpenCv operations")
st.subheader("Image operation")
st.write("This program is written to perform various operation on open cv")


add_select_sidebar = st.sidebar.selectbox("What operation would you like to perform? ",
                                          ("Gray Scale", "Blue", "Green", "Red", "Meshing"))

if add_select_sidebar == 'Gray Scale':
    image = st.sidebar.file_uploader("Upload file")

    if image is not None:
        image = Image.open(image)
        image = np.array(image)
        st.sidebar.image(image)
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        st.image(image)
elif add_select_sidebar == "Blue":
    image = st.sidebar.file_uploader("Upload file")

    if image is not None:
        image = Image.open(image)
        image = np.array(image)
        st.sidebar.image(image)
        zeros = np.zeros(image.shape[:2], dtype="uint8")
        r, g, b = cv.split(image)
        blue = cv.merge([zeros, zeros, b])
        st.image(blue)
elif add_select_sidebar == "Green":
    image = st.sidebar.file_uploader("Upload file")
    if image is not None:
        image = Image.open(image)
        image = np.array(image)
        st.sidebar.image(image)
        zeros = np.zeros(image.shape[:2], dtype="uint8")
        r, g, b = cv.split(image)
        green = cv.merge([zeros, g, zeros])
        st.image(green)
elif add_select_sidebar == "Red":
    image = st.sidebar.file_uploader("Upload file")
    if image is not None:
        image = Image.open(image)
        image = np.array(image)
        st.sidebar.image(image)
        zeros = np.zeros(image.shape[:2], dtype="uint8")
        r, g, b = cv.split(image)
        red = cv.merge([r, zeros, zeros])
        st.image(red)
elif add_select_sidebar == "Meshing":
    image = st.sidebar.file_uploader("Upload file")
    if image is not None:
        image = Image.open(image)
        image = np.array(image)
        st.sidebar.image(image)
        results = model_face_mesh.process(image)
        for landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(image, landmarks)
            st.image(image)



