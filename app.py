import discord
from discord.ext.commands import Bot
import asyncio
import sys
import re
import time
import json
from howdoi import howdoi

from flask import Flask, request
app = Flask(__name__)

def _howdoi(query):
    # Return this if no query provided along with howdoi prompt
    query_list = query.split(' ')
    if len(query_list) == 1:
        return 'Don\'t be shy, ask me anything!'
    response = howdoi.howdoi(vars(howdoi.get_parser().parse_args(query_list)))
    response = re.sub(r'\n\n+', '\n\n', response).strip() 
    return response 

def writeJSON(data):
    with open("logs.json", "w") as writeFile:
            json.dump(data, writeFile)

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

    content = message.content
    fullUser = message.author.name+'#'+message.author.discriminator
    print(content)
    content = content.lower()  

    r1 = content.find("howdoi")
    if r1 != -1:
        print("client call for howdoi")
        response = _howdoi(content)
        # Send the message 
        #botMsg = await message.channel.send("<@{}>, {}".format(message.author.id,_howdoi(content))) 
        embed = discord.Embed(title=" ".join(content.split(' ')[1:]), author=message.author.id, description=response)

        botMsg = await message.channel.send(embed=embed) 
       
        await botMsg.add_reaction('✅')
        await botMsg.add_reaction('❌')

       # then wait for which reaction they click
       # and go from there

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
    if (len(reaction.message.embeds) > 0):
        print("is an embed")
        # if it's an embed message
        msgContent = reaction.message.embeds[0].description
        # Target user is the user being mentioned
        targetUser = reaction.message.embeds[0].author
        
        if (reaction.emoji == "❌"):
            if ("717385516533809214" != str(user.id)):
                # the correct user reacted and didn't like the response
                data = {}
                data["user"] = "test"
                data["query"] = reaction.message.embeds[0].title
                data["response"] = msgContent
                data["time"] = int(time.time())               

                with open ("logs.json") as file:
                    jsonData = json.load(file)
                    temp = jsonData['logs']
                    temp.append(data)
                    writeJSON(jsonData)

    

# handle voice command in the future
@client.command(name="voice")
async def voice(ctx, arg):
    await ctx.send(arg)

# Get the last arg (the discord token)      
if len(sys.argv) > 1:
    client.run(sys.argv[len(sys.argv)-1])
else:
   print("Invalid args")
   print("Use: python app.py token")
