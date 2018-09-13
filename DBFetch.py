import sqlite3
import asyncio
import discord
from discord.ext import commands
import json
import datetime

bot = discord.Client()

with open('Vars.json', 'r') as v:
    vars = json.load(v)

db = sqlite3.connect('messages.sqlite')
c = db.cursor()
print(f'Connected to database.')

@bot.event
async def on_ready():
    print('Logged in.')
    await fetch()

async def fetch():
    g = bot.get_guild(365442290992545792)
    messages = 0
    for ch in g.channels:
        if isinstance(ch, discord.TextChannel):
            print(f'Starting {ch.name} at {datetime.datetime.now().time()}')
            try:
                async for m in ch.history(limit=None):
                    if m.author.bot == False:
                        messages += 1
                        if messages%50 == 0:
                            print(f'Parsed {messages} messages.')
                        if messages >= 1000:
                            db.commit()
                            messages = 0
                            print(f'Commiting - Parsed 1000 messages in {ch.name}.')
                        c.execute("INSERT INTO messages (message_id, user_id, user_name, content, guild_id, channel_id, channel_name) VALUES (?,?,?,?,?,?,?)",
                        (m.id, m.author.id, m.author.display_name, m.content, m.guild.id, m.channel.id, m.channel.name))
                print(f'Done with {ch.name} at {datetime.datetime.now().time()}')
            except Exception as e:
                print(f'Access forbidden for {ch.name} | {e}')
    db.commit()
    print('All done.')

#message_id int, user_id int, user_name text, content text, guild_id int, channel_id int, channel_name text


bot.run(vars['token'])

#db.commit()
#db.close()