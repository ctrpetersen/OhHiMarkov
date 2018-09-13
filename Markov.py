import asyncio
import markovify
import os
import json
import re
import discord
import sqlite3

db = sqlite3.connect('messages.sqlite')
c = db.cursor()

with open('Vars.json', 'r') as v:
    vars = json.load(v)

client = discord.Client()


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator}')

client.run(vars["token"])