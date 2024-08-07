import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import cv2
import numpy as np
from PIL import Image

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.frame = None

    def transform(self, frame):
        # Convert frame to BGR
        img = frame.to_ndarray(format="bgr24")
        self.frame = img
        return img

    def get_frame(self):
        if self.frame is not None:
            return Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

st.title("Webcam Photo Capture")

# Set up the video stream and transformer
ctx = webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

if ctx.video_transformer:
    st.video(ctx.video_transformer.get_frame(), use_column_width=True)

    if st.button("Capture Photo"):
        photo = ctx.video_transformer.get_frame()
        if photo:
            st.image(photo, caption="Captured Image", use_column_width=True)
