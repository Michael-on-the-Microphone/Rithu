
import os

import openai

count = 0
''' "\033[34m" + " " + "\n\033[0m " '''

openai.api_key = os.getenv("OPENAI_API_KEY")
print("\033[34m" + "How may I be of help?" + "\n\033[0m ")
print("\033[30m" + "you can type exit to leave anytime" + "\n\033[0m ")
while True:
  if count == 0:
    question = input()
    count = 1
  else:
    question = input("\033[34m" + "Anything else ?" + "\n\n\033[0m ")
    print("\n")
  '''print(question) question test'''
  if question.lower() == "exit":
    break
  print("\n")
  completeion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{
          "role":
          "system",
          "content":
          "You are an assistant. You will be called Rithu Answer the given Question"
      }, {
          "role": "user",
          "content": question
      }])
  print("\033[32m" + completeion.choices[0].message.content + "\n\033[0m")
print("\033[31m" + " Thanks, See ya soon !" + "\n\033[0m")
