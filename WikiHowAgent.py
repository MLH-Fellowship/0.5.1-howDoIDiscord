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
    how_tos = search_wikihow(Question, 1)
    assert len(how_tos) == 1
    
    Answer = "here i got you better answer from WikiHow"+str(how_tos[0])
    print(Answer)
  return Answer
