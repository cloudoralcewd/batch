from openai import OpenAI
client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1-mini",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {
            "role": "system",
            "content": "You are a expert in writing python program with PEP-8 Coding standards."
        },
        {
            "role": "user",
            "content": "Write python code for febonacci series."
        }
    ]
)

print(response.output_text)