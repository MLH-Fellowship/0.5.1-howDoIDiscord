import spacy
from pywikihow import WikiHow, search_wikihow


def WikiHowAgent(content) :
  #parse the question from the message to howdoi 
  pos = content.lower().find("!howdoi")
  #if no question was exist
  Question = content[pos+len("!howdoi"):]
  if Question.lower().find("--wikihow") :
    Question = Question.replace("--wikihow","")
  #pywikihow to find one answer 
  try :
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
  except :
      Answer = 0
  return Answer