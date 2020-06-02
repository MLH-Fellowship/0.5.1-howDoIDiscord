import discord
import asyncio
import sys

from flask import Flask, request
app = Flask(__name__)
@app.route('/posts', methods=['POST'])
def result():
    print(request.form['sched'])
    # Send a message to a discord text channel etc...
    return 'Received !'

client = discord.Client()

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


    if content[:6] == "howdoi":
       print("client call for howdoi")
    if content.startswith('!'):

        content = content[1:]
        if content.startswith('test'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have {} messages.'.format(counter))

# Get the last arg (the discord token)      
if len(sys.argv) > 1:
   client.run(sys.argv[len(sys.argv)-1])
else:
   print("Invalid args")
   print("Use: python app.py token")