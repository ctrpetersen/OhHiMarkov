import asyncio
import markovify
import os
import json
import re
import discord
from discord.ext import commands
import sqlite3

db = sqlite3.connect('messages.sqlite')
c = db.cursor()

with open('Vars.json', 'r') as v:
    vars = json.load(v)

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator}')

@client.event
async def on_message(message):
    if message.content == "-m":
        try:
            msg = await message.channel.send(f'Fetching messages for {message.author.name}#{message.author.discriminator}')
            c.execute("SELECT * FROM messages WHERE user_id=?",(message.author.id,))
            text = ''
            for m in c.fetchall():
                text += '\n' + m[3]
            text_model = markovify.NewlineText(text)
            sentence = text_model.make_sentence(tries=100)
            if sentence == None:
                sentence = f'Error - not enough messages to parse for {message.author.name}#{message.author.discriminator}'
            await msg.edit(content=(f'{message.author.name}#{message.author.discriminator} | `{sentence}`'))
        except Exception as e:
            await message.channel.send(f'Error - not enough messages to parse for {message.author.name}#{message.author.discriminator}')
            print(e)

client.run(vars['token'])