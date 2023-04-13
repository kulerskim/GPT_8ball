import os
import openai
from dotenv import load_dotenv

load_dotenv()

class GPT8Ball:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = "gpt-3.5-turbo"
        self.openai = openai
        self.openai.api_key = self.api_key

    def call_chat_completion(self, prompt):
        try:
            result = self.openai.ChatCompletion.create(model=self.model, messages=[{"role": "user", "content": prompt}])
            message = result["choices"][0]["message"]
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

if __name__ == "__main__":
    api_key = os.environ["GPT_8BALL_API_KEY"]
    gpt_ball = GPT8Ball(api_key)
    gpt_ball.run()