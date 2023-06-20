from dotenv import load_dotenv
import os
import openai


# You need to have .env file in the same directory as this file with you 
# OpenAI API key like this: OPENAI_API_KEY=your_api_key
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key

def chat_with_gpt(message):
    response = openai.Completion.create(
      engine="text-ada-001",
      prompt=message,
      temperature=0.5,
      max_tokens=100
    )

    return response.choices[0].text.strip()

user_message = input("User: ")
gpt_response = chat_with_gpt(user_message)
print("GPT: ", gpt_response)