import models.customdice as customdice
import discord
from discord.ext import commands


### VARIABLES ###
#TOKEN = 
client = commands.Bot(command_prefix='.')

### FUNNCTIONS ###


@client.event
async def on_ready():
    print(f"\a\tConectado como {client.user.name}")


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


### MAIN ###

# connect
client.run(TOKEN)
