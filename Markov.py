import asyncio
import os
import json
import re
import discord
from discord.ext import commands

with open('Vars.json', 'r') as v:
    vars = json.load(v)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator}')

bot.run(vars["token"], bot=True, reconnect=True)