import openai
import os
import json
from better_profanity import profanity
import sys ## from sys import exit

## FOR THE CENSOR
if __name__ == "__main__":
    profanity.load_censor_words()

## SET UP API KEY
ai_key = os.environ['open_ai_key']

## SET THE KEY TO THE KEY THEN DEF OPEN_AI FUNCTION (RESPONSE)
openai.api_key = ai_key
def open_ai(content):
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=content,
  temperature=0.5,
  max_tokens=1000,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  )
  json_data = json.loads(str(response))
  text = (str(json_data['choices'][0]['text']))
  return text


## DEF THE ASK AI FUNCTION WHICH RUNS THE QUESTIONS
def askAi():
  type = str(input("A story or letter or other?: "))
  abto = str(input("A " + type + " about or to someone?: "))
  abto = abto.lower()
  if abto == "to":
    about = str(input("A " + type +  " " + abto + " and about" + "?: "))
  else:
    about = str(input("A " + type +  " " + abto + "?: "))
    
  content = ("make a 1000 word" + type + " " + abto + about)

  #.lower() the words
  type = type.lower()
  about = about.lower()
  content = content.lower()
  response = open_ai(content)
  censored_response = profanity.censor(response) ## run the censor
  print(censored_response) ## print the censored text
  


## loop constantly until it's time to quit
while True:
  askAi()
  quit = input("Would you like to quit, y/n?: ")
  quit = quit.upper()
  if quit == "Y":
    sys.exit
    break
  else:
    print("Continuing")
  print("")
