import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
 
@bot.command()
async def admin(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)
    
@bot.command()
async def repetir(ctx, *, content):
    await ctx.send(content)

bot.run("SECRET TOKEN")
