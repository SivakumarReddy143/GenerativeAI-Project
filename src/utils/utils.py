import pyttsx3
import speech_recognition as sr
import sys
from src.exception.exception import GenerativeAIException

class TextToSpeech:
    def text_to_speech(self,text):
        try:
            engine=pyttsx3.init()
            engine.say(text=text)
            engine.runAndWait()
        except Exception as e:
            raise GenerativeAIException(e,sys)
        
class SpeechToText:
    def speech_to_text(self):
        recognizer=sr.Recognizer()
        tts=TextToSpeech()
        
        with sr.Microphone() as source:
            tts.text_to_speech("adjusting ambient Noises. please wait....")
            recognizer.adjust_for_ambient_noise(source,duration=2)
            tts.text_to_speech('Listinging...')
            try:
                audio=recognizer.listen(source,timeout=10)
                tts.text_to_speech("Recognising...")
                text=recognizer.recognize_google(audio)
                print(f"recognised text:\n{text}")
                return text
            except Exception as e:
                raise GenerativeAIException(e,sys)
                