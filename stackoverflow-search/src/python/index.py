# connect to openai api and get the response
# from the api
def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    return response

# write a python program to get the response from the api and print it
def print_response(prompt):
    response = get_response(prompt)
    print(response.choices[0].text)

# write a python program to get the response from the api and return it

def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    return response.choices[0].text

def setupAPI():
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    setupAPI()
    prompt = "Human: Hello, who are you?\nAI:"
    print_response(prompt)