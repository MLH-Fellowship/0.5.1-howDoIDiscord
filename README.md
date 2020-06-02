# 0.5.1-howDoIDiscord
Discord bot for howdoi

## Flow of a basic call
![Architecture of this app showing the flow of a query from user to response](https://i.imgur.com/jtVVdTl.png)
![Architecture of this app in terms of it's elements](https://i.imgur.com/tT5vu3A.png)
# Installation
## Discord bot
1. `cd discordBot && npm install dotenv discord.js node-fetch`
2. `touch .env`. Inside this .env file put in `token="discordTokenHere"`. The discordTokenHere is the token for the bot that is pinned in the howDoI discord. If this get's leaked anyone can do anything with our bot so keep it safe.
2. `node main.js`

The bot is now listening for messages in the channel and will log them to console
 