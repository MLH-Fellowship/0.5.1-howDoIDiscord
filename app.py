  
import discord
from discord.ext.commands import Bot
import asyncio
import sys
import re
import time
import json
from howdoi.howdoi import howdoi
from datetime import datetime
from dotenv import load_dotenv
from parser import _set_params

from WikiHowAgent import Question_generate, WikiHowAgent

from flask import Flask, request
import os
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
app = Flask(__name__)

def _howdoi(query):
    response = howdoi(_set_params({'query':query}))
    response = re.sub(r'\n\n+', '\n\n', response).strip() 
    return response

def writeJSON(data):
    with open("logs.json", "w") as writeFile:
        json.dump(data, writeFile)


def logCall(query, user, roundTripTime):
    print("[{}] {} - {} {}ms".format(datetime.now(), user, query, roundTripTime))


async def callHowDoI(message, index, substr, testing):
    startTime = int(round(time.time() * 1000))
   
    content = message.content
    fullUser = message.author.name+'#'+message.author.discriminator
    content = content.lower() 

    if not testing:
        if ((index + len(substr) == len(content))):
            res = 'Don\'t be shy, ask me anything!'
        else:
            res = _howdoi(content)
        response = "<@{}>, {}".format(message.author.id, res)
        embed = discord.Embed(title=" ".join(content.split(substr, 1)[1:]), description=response, color=discord.Color.green())

        try:
            botMsg = await message.channel.send(embed = embed)
        except discord.DiscordException as err:
            print("Oops! {}".format(err))
        else:
            endTime = int(round(time.time() * 1000))
            logCall(content, fullUser,endTime-startTime)
            await botMsg.add_reaction('✅') 
            await botMsg.add_reaction('❌') 
     
    else:
        # Escape the url encoded characters such as %20
        unescapedQuery = message["query"].replace("%20", " ")
        response = "<@{}>, {}".format(message["author"], _howdoi(unescapedQuery))
        return response


# Route made for testing the system through HTTP requests
@app.route('/test', methods=["POST"])
def test():
    testQuery = request.args.get('testquery') 
    if not testQuery:
        return {
            "status":"error",
            "body":"invalid paramaters"
            }, 400
    if testQuery[:6] != "howdoi":
          return {
            "status":"error",
            "body":"howdoi keyword not found"
            }, 400


    testMessage = {
        "author":"test",
        "query": testQuery
    }
   
    testCall = loop.run_until_complete(callHowDoI(testMessage, 0, "", True))
    return {
        "status":"success",
        "body": testCall
    }, 200


@app.route('/posts', methods=['POST'])
def result():
    print(request.form['sched'])
    # Send a message to a discord text channel etc...
    return 'Received !'

client = Bot(command_prefix = "$")

@client.event
async def on_ready():
    print('Logged in as {} - {}'.format(client.user.name, client.user.id))
    print('------')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    content = message.content.lower()
    substr = "howdoi"

    r1 = content.rfind(substr) # get the last occurrence of substr in case people specify multiple
    if r1 != -1:
        await callHowDoI(message, r1, substr, False)

    elif content.startswith('!'):
        content = content[1:]
        if content.startswith('test'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have {} messages.'.format(counter))

@client.event
async def on_reaction_add(reaction,user):
   if (len(reaction.message.embeds) > 0):        # if it's an embed message
        msgContent = reaction.message.embeds[0].description
       
        # Target user is the user being mentioned
        targetUser = reaction.message.embeds[0].description.split(',')[0]
       
        if (reaction.emoji == "❌"):
            if ("717385516533809214" != str(user.id)):
                # A user reacted and didn't like the response
                data = {}                
                data["user"] = targetUser
                data["query"] = reaction.message.embeds[0].title
                data["response"] = msgContent
                data["time"] = int(time.time())               

                with open ("logs.json") as file:
                    jsonData = json.load(file)
                    temp = jsonData['logs']
                    temp.append(data)
                    writeJSON(jsonData)

                # Query the wikihow api and get a better response hopefully
                # to give the user
                async with reaction.message.channel.typing():
                    # await it's response then send it in am embed
                    wikiHowResponse = WikiHowAgent(reaction.message.embeds[0].title)
                   
                    embed = discord.Embed(title="Here's a wiki how answer instead",
                                        description=wikiHowResponse,
                                        color=discord.Color.green())
                    embed.set_footer(text=wikiHowResponse)
                    await reaction.message.channel.send(embed=embed)
                   
               
# handle voice command in the future
@client.command(name="voice")
async def voice(ctx, arg):
    await ctx.send(arg)


# If testing env variable set it means the script
# is unit testing and only needs the flask server
# not the discord bot
if os.getenv("TESTING"):
    print("In testing mode")
    loop = asyncio.get_event_loop()
    app.run()
else:
    print("In discord mode")
    client.run(TOKEN)