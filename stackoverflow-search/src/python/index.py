# connect to openai api and get the response
# from the api
import requests


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


def setup_api():
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")


def get_joke():
    return requests.get(
        "https://icanhazdadjoke.com/", headers={'Accept': 'text/plain'})


def main():
    setup_api()
    prompt = "Human: Hello, who are you? I'm a Robot\nAI:"
    print_response(prompt)
    response = get_joke()
    if response.status_code == 200:
        print(response.text)


if __name__ == "__main__":
    main()
