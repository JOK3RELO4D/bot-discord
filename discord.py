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


@bot.command()
async def reglas(ctx):
    reglas = [
        "1. Se respetuoso, esta es una comunidad.",
        "2. Manten seguridad y no compartas informacion personal",
        "3. Mantener los debates y conversaciones en un tono respetuoso.",
        "4. No compartir contenido inapropiado .",
        "5. No hacer spam de contenido o imagenes.",
        "6. Utilizar los canales adecuados para cada tipo de contenido.",
        "Recuerda que infrigir en estos aspectos puede generar una sancion :)",
    ]
    
    mensaje = "Reglas del servidor:\n\n" + "\n".join(reglas)
    await ctx.send(mensaje)

bot.run("Secret code")
