import streamlit as st
from streamlit_webrtc import ClientSettings, VideoTransformerBase, VideoProcessorBase, RTCConfiguration, WebRtcMode, webrtc_streamer
import av
from imutils import face_utils
import dlib
import cv2

st.title("Streamlit WebRTC using DLIB")
st.write("This is a sample to integrate DLIB :D ")


p = 'shape_predictor_68_face_landmarks.dat'

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
        
    for (i, rect) in enumerate(rects):
        s = predictor(gray, rect)
        s = face_utils.shape_to_np(s)

        for(i, y) in s:
            cv2.circle(img, (i,y), 2, (0, 255, 0), -1)

    # ... Image processing, or whatever you want ...

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)

