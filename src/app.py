import os
import models.customdice as customdice
from dotenv import load_dotenv
from discord.ext import commands


### VARIABLES ###

# get discord token from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# set discord client with commands prefix
client = commands.Bot(command_prefix='.')


### FUNNCTIONS ###
@client.event
async def on_ready():
    print(f"\a\tConectado como {client.user.name}")


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


@client.command(name="d")
async def dice_roll(ctx, ring, skill):
    converted = customdice.convert(ring=ring, skill=skill)
    dicepool = customdice.dice_roller(
        d6=converted["ring"], d12=converted["skill"])

    result = customdice.format(ring=dicepool["d6"], skill=dicepool["d12"])
    result = f"Ring Dice: {result['ring']}\nSkill Dice: {result['skill']}"

    await ctx.send(result)


@client.command(name="r")
async def ring_roll(ctx, ring):
    converted = customdice.convert(ring=ring)
    dicepool = customdice.dice_roller(d6=converted["ring"])

    result = customdice.format(ring=dicepool["d6"])
    result = f"Ring Dice: {result['ring']}"

    await ctx.send(result)


@client.command(name="s")
async def skill_roll(ctx, skill):
    converted = customdice.convert(skill=skill)
    dicepool = customdice.dice_roller(d12=converted["skill"])

    result = customdice.format(skill=dicepool["d12"])
    result = f"Skill Dice: {result['skill']}"

    await ctx.send(result)


### MAIN ###

# connect
client.run(DISCORD_TOKEN)
# ring="2"
# skill="3"

#converted = customdice.convert(ring=ring)
#dicepool = customdice.dice_roller(d6=converted["ring"])

#result = customdice.format(ring=dicepool["d6"])
#result = f"Ring Dice: {result['ring']}\nSkill Dice: {result['skill']}"
#print(result)
