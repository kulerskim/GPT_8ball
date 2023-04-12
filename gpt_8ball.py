import os
import openai
from dotenv import load_dotenv

load_dotenv()

def call_gpt4_api(prompt):
    openai.api_key = os.environ["GPT_8BALL_API_KEY"]

    result = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    message = result["choices"][0]["message"]
    return message["content"]

def main():
    print("Welcome to GPT-8Ball!")
    while True:
        user_input = input(">> ")
        response = call_gpt4_api(user_input)
        print("GPT-8Ball: ", response)

if __name__ == "__main__":
    main()