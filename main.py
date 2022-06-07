import openai
import os
import json
from better_profanity import profanity

if __name__ == "__main__":
    profanity.load_censor_words()
  
ai_key = os.environ['open_ai_key']
#make a #### word #### about #####

openai.api_key = ai_key
def open_ai(content):
  #print("open_ai opened")
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=content,
  temperature=0.5,
  max_tokens=1000,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  #stop=[""]
  )
  #print(response)
  json_data = json.loads(str(response)) #(response.text)
  #print(json_data['choices']['text'])
  text = (str(json_data['choices'][0]['text']))
  return text



def askAi():
  type = str(input("A story or letter or other?: "))
  abto = str(input("A " + type + " about or to someone?: "))
  abto = abto.lower()
  if abto == "to":
    about = str(input("A " + type +  " " + abto + " and about" + "?: "))
  else:
    about = str(input("A " + type +  " " + abto + "?: "))
    
  content = ("make a 1000 word" + type + " " + abto + about)
  
  size = size.lower()
  type = type.lower()
  about = about.lower()
  content = content.lower()
  response = open_ai(content)
  censored_response = profanity.censor(response)
  print(censored_response)
  #print(response)
  


#ask = input("Story: ") ## make a 5000 word letter about being sorry for doing war crimes

while True:
  askAi()
  print("")
