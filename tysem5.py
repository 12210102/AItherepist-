import streamlit as st
import openai
from transformers import pipeline
import cv2
from fer import FER
from PIL import Image
import numpy as np
from PIL import Image

# OpenAI API key configuration (add your API key here)
openai.api_key = "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"

# Load pre-trained emotion classifier model for text-based analysis
text_emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Load face emotion recognition model
detector = FER(mtcnn=True)

# Function to analyze text emotions using OpenAI GPT
def analyze_text_emotion(user_input):
    emotion_analysis =text_emotion_classifier(user_input)
    emotion_label = emotion_analysis[0]['label']
    emotion_score = emotion_analysis[0]['score']
    return emotion_label, emotion_score

def preprocess_image(image_input):
    img = Image.open(image_input) if not isinstance(image_input, np.ndarray) else Image.fromarray(image_input)
    if img.mode=='RGBA':
        img = img.convert('RGB')
    img_array=np.array(img)
    return img_array

# Function to analyze face emotion
def analyze_face_emotion(image):
    detector=FER(mtcnn=True)
    emotion, score = detector.top_emotion(image)
    return emotion, score

# Streamlit UI
st.title("AI Therapist: Text and Face Emotion Detection")

# Sidebar for user selection
st.sidebar.title("Select Input Type")
input_type = st.sidebar.radio("Choose input method:", ("Text Input", "Image Upload","Use Camera"))

# Text-based emotion detection
if input_type == "Text Input":
    st.header("Text-based Emotion Recognition")
    user_input = st.text_area("How are you feeling today?")

    if st.button("Analyze Emotion"):
        if user_input:
            # Analyze text using the AI therapist and emotion classifier
            emotion_analysis = text_emotion_classifier(user_input)
            gpt_analysis = analyze_text_emotion(user_input)
            emotion,confidence=analyze_text_emotion(user_input)

            st.subheader("Emotion Analysis (Text):")
            st.write(f"Predicted Emotion: {emotion_analysis[0]['label']}")
            st.write(f"Emotion Confidence: {emotion_analysis[0]['score']:.2f}")

            st.subheader("GPT-based Emotion Insight:")
            st.write(gpt_analysis)
        else:
            st.error("Please enter some text for analysis.")

# Face-based emotion detection
elif input_type == "Image Upload":
    st.header("Face Emotion Recognition")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Convert uploaded image to OpenCV format
        img_array=preprocess_image(uploaded_file)
        img_array = np.array(img_array)

        st.image(img_array, caption="Uploaded Image", use_column_width=True)

        # Detect and analyze face emotion
        emotion, score = analyze_face_emotion(img_array)

        st.subheader("Emotion Analysis (Face):")
        st.write(f"Predicted Emotion: {emotion}")
        st.write(f"Emotion Confidence: {score:.2f}")

elif input_type== 'Use Camera':
    st.write("Using your camera to detect face emotion. Click the button below to capture.")
    camera_button=st.button("capture the button")
    if camera_button:
        cap=cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("could not open camera")
        else:
            ret,frame=cap.read()
            cap.release()
            if ret:
                img_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                st.image(img_rgb,caption="captured image",use_column_width=True)
                emotion,score=analyze_face_emotion(img_rgb)
                st.subheader("Emotion Analysis (Face):")
                st.write(f"predicted emotion:{emotion}")
                st.write(f"emotion confidence:{score:2f}")
            else:
                st.error("failed o capture image from camera")

# Footer
st.sidebar.title("About")
st.sidebar.info("This AI Therapist app uses OpenAI GPT and Facial Emotion Recognition to detect emotions from both text and images.")
