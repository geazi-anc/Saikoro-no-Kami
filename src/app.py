from models.customdice import CustomDice
from dotenv import load_dotenv
from discord.ext import commands
from os import getenv


##### VARIABLES #####

# load enviroment variables from .env file
load_dotenv()

# get discord token from enviroment
DISCORD_TOKEN = getenv("DISCORD_TOKEN")

# set discord client with commands prefix
client = commands.Bot(command_prefix='.')


##### FUNNCTIONS #####
@client.event
async def on_ready():
    print(f"\a*We are already online, connected as {client.user.name}!*")


@client.command(help="Check if bot is on.")
async def ping(ctx):
    await ctx.send("PONG!")


@client.command(name="d", help="Roll a quantity of ring and skill dice. Example: *.d 3 3*, roll three ring dice plus three skill dice.")
async def dice_roll(ctx, ring, skill):
    dice = CustomDice(ring=ring, skill=skill)
    result = dice.format(**dice.roll())

    await ctx.send(result)


@client.command(name="r", help="Roll a quantity of ring dice only. Example: *.r 3*, roll three ring dice.")
async def ring_roll(ctx, ring):
    dice = CustomDice(ring=ring, skill=0)
    result = dice.format(**dice.roll())
    result = result.splitlines()[0]

    await ctx.send(result)


@client.command(name="s", help="Roll a quantity of skill dice only. Example: *.s 3*, roll 3 skill dice.")
async def skill_roll(ctx, skill):
    dice = CustomDice(ring=0, skill=skill)
    result = dice.format(**dice.roll())
    result = result.splitlines()[1]

    await ctx.send(result)


@client.command(name="t", help="Show table of emojis meanings.")
async def table(ctx):
    table = "👏 > Success;\n🎆 > Explosive Success;\n😫 > Strife;\n🤔 > Opportunity;\n◻ > Blank Face;"

    await ctx.send(table)


##### MAIN #####

# connect
client.run(DISCORD_TOKEN)
