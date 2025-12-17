from openai import OpenAI
client = OpenAI(api_key="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")

prompt = "Hello, how are you?"

completion = client.chat.completions.create(
  model="gpt-5.2",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)
