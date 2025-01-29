import streamlit as st
import requests
import speech_recognition as sr

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000/predict"

def transcribe_audio():
    """
    Capture and transcribe audio input from the user.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak your symptoms.")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, could not understand your audio. Please try again.")
        except sr.RequestError as e:
            st.error(f"Error with speech recognition service: {e}")
        return None

st.title("Disease Prediction Chatbot")
input_method = st.radio("Choose input method:", ["Text", "Audio"])

if "user_input" not in st.session_state:
    st.session_state.user_input = None

if input_method == "Text":
    st.session_state.user_input = st.text_input("Describe your symptoms:")

elif input_method == "Audio":
    if st.button("Record Audio"):
        transcribed_text = transcribe_audio()
        if transcribed_text:
            st.session_state.user_input = transcribed_text
            st.success(f"Transcribed Symptoms: {transcribed_text}")

if st.button("Predict"):
    if st.session_state.user_input:
        response = requests.post(BACKEND_URL, json={"symptoms": st.session_state.user_input})

        if response.status_code == 200:
            result = response.json()
            st.write(f"**Predicted Disease:** {result['disease_info']}")
            st.write(f"**AI Response:** {result['response']}")
        else:
            st.error("No matching disease found.")
