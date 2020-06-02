const Discord = require('discord.js');
const client = new Discord.Client();
const fetch = require('node-fetch');

require('dotenv').config();

client.once('ready', () => {
    console.log('Ready!');
});

client.login(process.env.token);

client.on('message', message => {
    const msg = message.content;

    if (msg.startsWith('howdoi')) {
        // message should be intercepted it had the howdoi keyword
        const query = msg.slice(7, );
        // message.reply(`You actived me and said "${query}"`);

        // Send the query to the flask server and await a response
        // for now we'll just use a test endpoint to get data back

        fetch('https://jsonplaceholder.typicode.com/todos/1')
            .then(response => response.json())
            .then(res => {
                message.reply(`[${res.id}] ${res.title}`)
            }, (err) => {
                message.reply(`There was an error calling the test API`);
                console.log(err)
            });
    }
});