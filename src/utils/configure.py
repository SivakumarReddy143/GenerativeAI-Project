import os
import sys
import google.generativeai as genai
from src.exception.exception import GenerativeAIException
from dotenv import load_dotenv
load_dotenv()

class GenAIConfigure:
    def configure(self):
        try:
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            model=genai.GenerativeModel("gemini-1.5-flash")
            return model
        except Exception as e:
            raise GenerativeAIException(e,sys)