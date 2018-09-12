import sqlite3
import asyncio
import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='-', description='Fetches all messages in a server and adds it to a SQLite DB.')

with open('Vars.json', 'r') as v:
    vars = json.load(v)

db = sqlite3.connect('messages.sqlite')
print(f'Connected to database.')

@bot.event
async def on_ready():
    print('Logged in.')
    await fetch()

async def fetch():
    g = bot.get_guild(365442290992545792)
    for ch in g.channels:
        if isinstance(ch, discord.TextChannel):
            messages = await ch.history().flatten()
            for m in messages:
                if m.author.bot == False:
                    print(m)



bot.run(vars['token'])

#db.commit()
#db.close()