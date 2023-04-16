import os
import openai
import speech_recognition as sr
from dotenv import load_dotenv

from conversation_history import ConversationHistory
from polly_text_to_speech import PollyTextToSpeech

from config import LANGUAGE
from config import PROMPT

load_dotenv()

class GPT8Ball:
    def __init__(self):
        self.api_key = os.environ["GPT_8BALL_API_KEY"]
        self.model = "gpt-3.5-turbo"
        self.conversation_history = ConversationHistory()
        self.tts = PollyTextToSpeech(language = LANGUAGE)
        self.openai = openai
        self.openai.api_key = self.api_key

    def call_chat_completion(self, prompt):
        try:
            self.conversation_history.add({"role": "user", "content": prompt})
            result = self.openai.ChatCompletion.create(model=self.model, messages=self.conversation_history.get().copy())
            message = result["choices"][0]["message"]
            self.conversation_history.add(message)
            return message["content"]
        except self.openai.error.OpenAIError:
            return "Oops, there was an error processing your request. Please try again."
        

    def get_audio_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
            return None

    def run(self):
        print("Welcome to GPT-8Ball! Press Ctrl+C to exit.")
        self.conversation_history.add({"role": "system", "content": PROMPT})
        self.openai.ChatCompletion.create(model=self.model, messages=self.conversation_history.get().copy())
        
        while True:
            try:
                user_input = self.get_audio_input()
                if user_input is not None:
                    response = self.call_chat_completion(user_input)
                    print("GPT-8Ball: ", response)
                    self.tts.speak(response)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
