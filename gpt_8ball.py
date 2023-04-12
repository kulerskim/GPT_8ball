import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["GPT_8BALL_API_KEY"]

def call_gpt4_api(prompt):
    try:
        result = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        message = result["choices"][0]["message"]
        return message["content"]
    except openai.error.OpenAIError:
        return "Oops, there was an error processing your request. Please try again."

def main():
    print("Welcome to GPT-8Ball! Press Ctrl+C to exit.")
    while True:
        try:
            user_input = input(">> ")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        response = call_gpt4_api(user_input)
        print("GPT-8Ball: ", response)

if __name__ == "__main__":
    main()