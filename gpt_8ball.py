import os
import openai
from dotenv import load_dotenv

from conversation_history import ConversationHistory
from text_to_speach import TextToSpeach

load_dotenv()

class GPT8Ball:
    def __init__(self):
        self.api_key = os.environ["GPT_8BALL_API_KEY"]
        self.model = "gpt-3.5-turbo"
        self.conversation_history = ConversationHistory()
        self.tts = TextToSpeach()
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

    def run(self):
        print("Welcome to GPT-8Ball! Press Ctrl+C to exit.")
        while True:
            try:
                user_input = input(">> ")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            response = self.call_chat_completion(user_input)
            print("GPT-8Ball: ", response)
            self.tts.speak(response)
