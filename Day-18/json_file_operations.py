# {key1: val1, key2:val2, key3: val3 }

# JSON HANDLING FOR STRUCTURED DATA

import json
import requests

with open("./config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(type(data))

    print(data["retry_policy"]["initial_delay"])
    print(data["user_prompts"]["farewell_message"])

    print(f"Keys => {data.keys()}")
    print(f"Values =>  {data.values()}")

response = requests.get('https://jsonplaceholder.typicode.com/post')
print(response)

if response.status_code == 200:
    data = json.loads(response.text)
    print(data[1]['title'])

    for record in data:
        print(record["title"])
else:
    print(f"Request Faild =>  {response.status_code}")


response = {
    "usage": {
        "total_tokens": 1000,
        "details": {"prompt_tokens": 300, "completion_tokens": 700}
    },
    "choices": [
        {"text": "The capital of France is Paris.", "index": 0},
        {"text": "France's capital is Paris.", "index": 1}
    ]
}

print(response["usage"]["details"]["completion_tokens"])
print(response["usage"]["total_tokens"])

print(response["choices"][0]["text"])
print(response["choices"][1]["text"])







