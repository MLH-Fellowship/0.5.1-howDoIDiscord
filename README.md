# 0.5.1-howDoIDiscord
Discord bot for howdoi

## Flow of a basic call
![Architecture of this app showing the flow of a query from user to response](https://i.imgur.com/jtVVdTl.png)
![Architecture of this app in terms of it's elements](https://i.imgur.com/tT5vu3A.png)
# Installation
## Discord bot
1.create a virtualenv and initialize it. This may vary depending on your operating system. 

  `virtualenv env && source env/bin/activate`
  
2.Install dependencies using pip.
  `pip install -r requirements.txt`
3.Run the app with the following:

  `export FLASK_APP=main.py && flask run`
  
once Flask app start The bot is now listening for messages in the channel and will log them to console
Web at localhost:5000.
