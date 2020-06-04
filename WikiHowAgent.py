import spacy
from pywikihow import WikiHow, search_wikihow

def Question_generate(content):
  verb  = []
  noun = []
  nlp = spacy.load("en_core_web_sm")
  pos = content.lower().find("howdoi")
  Q_Token = nlp(content[pos+len("howdoi"):])
  for token in Q_Token :
    if token.pos_ == "VERB":
      verb.append(token)
  if len(verb) !=0:
      v_pos = content.lower().find(verb[0].text)
      QUESTION = "how to "+content[v_pos:]
      print(QUESTION)
  else :
    QUESTION = "EMPTY"
  return QUESTION


def WikiHowAgent(content) :
  #parse the question from the message to howdoi 
  Question = Question_generate(content)
  #if no question was exist
  if Question == "EMPTY" :
    Answer = 0
  #pywikihow to find one answer 
  else :
    how_tos = search_wikihow(Question,1)
    how_to = how_tos[0].as_dict()
    n_step = how_to['n_steps']
    steps = how_to['steps']
    if n_step < 20 :
      summary = []
      for i in range(n_step) :
        summary.append(steps[i]['summary'])
      summary ='\n'.join([str(elem) for elem in summary])
      Answer = summary
    else :
      summary = []
      for i in range(20) :
        summary.append(steps[i]['summary'])
      summary ='\n'.join([str(elem) for elem in summary])
      Answer = summary + " \n \n Check this link for more results: " + how_to['url']
  return Answer

