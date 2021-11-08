from models.customdice import CustomDice
from dotenv import load_dotenv
from discord.ext import commands
from os import getenv


##### VARIABLES #####

# load enviroment variables from .env file
load_dotenv()

# get discord token from enviroment system
DISCORD_TOKEN = getenv("DISCORD_TOKEN")

# set discord client with commands prefix
client = commands.Bot(command_prefix='.')


##### FUNNCTIONS #####
@client.event
async def on_ready():
    print(f"\a*We are already online, connected as {client.user.name}!*")


@client.command()
async def ping(ctx):
    await ctx.send("PONG!")


@client.command(name="d")
async def dice_roll(ctx, ring, skill):
    dice = CustomDice(ring=ring, skill=skill)
    result = dice.format(**dice.roll())

    await ctx.send(result)


@client.command(name="r")
async def ring_roll(ctx, ring):
    dice = CustomDice(ring=ring, skill=0)
    result = dice.format(**dice.roll())
    result = result.splitlines()[0]

    await ctx.send(result)


@client.command(name="s")
async def skill_roll(ctx, skill):
    dice = CustomDice(ring=0, skill=skill)
    result = dice.format(**dice.roll())
    result = result.splitlines()[1]

    await ctx.send(result)


##### MAIN #####

# connect
client.run(DISCORD_TOKEN)
