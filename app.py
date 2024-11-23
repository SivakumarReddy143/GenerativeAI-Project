from src.logging.logger import logging
from src.exception.exception import GenerativeAIException
from src.utils.utils import TextToSpeech,SpeechToText
from src.utils.configure import GenAIConfigure
from src.main.main import GenerativeAIResponse
import sys
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai



class UploadImage:
    def uploaded_image(self):
        uploaded_file=st.file_uploader("choose an image...",type=["jpg","jpeg","png"])
        image=""
        if uploaded_file is not None:
            image=Image.open(uploaded_file)
            st.image(image,caption="Uploaded Image.",use_container_width=True)
            logging.info("Image added successfully")
        return image


if __name__ == "__main__":
    try:
        st.set_page_config(page_title="Image Analysis")
        st.header("Gemini Application")

        
        if "model" not in st.session_state:
            st.session_state.model = None

        tts = TextToSpeech()
        stt = SpeechToText()

        
        if st.button("Configure AI Model"):
            tts.text_to_speech("Configuring Google Generative AI Model")
            logging.info("Configuring Google Generative AI Model")
            config = GenAIConfigure()
            st.session_state.model = config.configure()
            st.success("Model configured successfully!")
            logging.info("Model configured successfully!")

        
        if st.session_state.model is None:
            st.warning("Please configure the AI model first.")
        else:
            
            upload_image = UploadImage()
            image = upload_image.uploaded_image()

            if image:
                tts.text_to_speech("Image uploaded successfully. Please ask AI any question related to the image.")
                
                
                input_text = ""
                if st.button("Speak Your Question"):
                    input_text = stt.speech_to_text()

                if input_text:
                    ai = GenerativeAIResponse()
                    logging.info("Generated response using Gemini")
                    response = ai.get_gemini_respone(
                        input=input_text, 
                        image=image, 
                        model=st.session_state.model
                    )
                    st.subheader("The Response is:")
                    st.write(response)
                    tts.text_to_speech(response)

    except Exception as e:
        st.error(f"An error occurred: {e}")
        raise GenerativeAIException(e, sys)
