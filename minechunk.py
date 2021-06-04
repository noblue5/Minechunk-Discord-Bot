# Minechunk bot
# Coded by noblue5

# // Imports \\

import discord
from discord.ext import commands
from idlelib import query
import requests

# // Important stuff \\

client = commands.Bot(command_prefix='m!')
client.remove_command('help')
version = "Private testing"


# // On_ready Event \\

@client.event
async def on_ready():
    print('Minechunk has been started...')
    await client.change_presence(activity=discord.Game(version))


# // Bot Token \\ (Not a command)

client.run('(token here)')
