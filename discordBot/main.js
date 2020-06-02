const Discord = require('discord.js');
const client = new Discord.Client();

require('dotenv').config();

client.once('ready', () => {
    console.log('Ready!');
});

client.login(process.env.token);

client.on('message', message => {
    console.log(message.content);
});