from src.exception.exception import GenerativeAIException
import sys

class GenerativeAIResponse:
    def get_gemini_respone(self,input,image,model):
        try:
            if input!="":
                response=model.generate_content([input,image])
            else:
                response=model.generate_content(image)
            return response.text
        except Exception as e:
            raise GenerativeAIException(e,sys)