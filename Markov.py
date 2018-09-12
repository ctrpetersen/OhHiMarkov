import asyncio
import markovify
import os
import json
import re
import discord

messages_to_fetch = 500

with open('Vars.json', 'r') as v:
    vars = json.load(v)

client = discord.Client()

#def get_messages_from_user(member_to_get):

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator}')

client.run(vars["token"])