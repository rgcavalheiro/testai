import json
import os
import openai

openai.api_key = 'api_key'



stop = ""
while(stop!="exit"):
  stop = input("Human: ")
  response = openai.Completion.create(
    engine="davinci",
    prompt="\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman:" + stop + "\n AI:",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["\n", " Human:", " AI:"]
  )

  print(response.choices)


