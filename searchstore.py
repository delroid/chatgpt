# Using chatgpt via api
# Search and store results in a text file

import openai

openai.api_key = "<put your chatgpt api key here>"

#input chapter name 
query2 = input("Enter title for document:")

#input new chapter contect
query = input("new chapter question?:")

response = openai.Completion.create(
  model="text-davinci-003",
  #model="code-davinci-002",
  prompt=query,
  temperature=0.9,
  max_tokens=1200,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

lines = response.choices[0].text

with open(f"{query2}.txt", 'w') as f:
    f.writelines(lines)
