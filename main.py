import openai

# load and set our key
openai.api_key = open("key.txt", "r").read().strip("\n")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
  messages=[{"role": "user", "content": "What is the circumference in km of the planet Earth?"}]
)