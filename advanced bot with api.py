import requests 
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user} disfruta el server!')
    
@bot.command()
async def bye(ctx):
    await ctx.send(f'Hasta luego :v')

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

@bot.command()
async def borrar(ctx, cantidad: int):
    await ctx.channel.purge(limit=cantidad + 1)
    
@bot.command()
async def helplease(ctx):
    lista = [
        "$hello: Te da la bienvenida el bot.",
        "$heh: Repite por cinco veces el texto que escribas.",
        "$admin: El bot escribe un mensaje en tu nombre.",
        "$repetir: Repite el mensaje que escribas.",
        "$reglas: Muestra la lista de reglas del servidor.",
        "$helplease: Muestra la lista actual de códigos existentes en el servidor.",
        "$mensaje: Ofrece un saludo de hola diferente.",
        "$borrar: Introduce el número de mensajes que deseas eliminar.",
        "Puedes utilizar estos comandos según tus necesidades.",
    ]
    mensaje = "Facilidades del bot!:\n\n" + "\n".join(lista)
    await ctx.send(mensaje)

@bot.command()
async def mensaje(ctx):
    holas = [
         "Hola!", 
         "Hola", 
         "Hola, ¿cómo estás?",
         "!Hola, ¿qué tal?!",
         "!Hola, bienvenido!",
         "Hola, ¿cómo te encuentras?",
        ]
    await ctx.send(random.choice(holas))

@bot.command()
async def adios(ctx):
    adios = [
        "¡Hasta luego!",
        "¡Adiós!",
        "¡Nos vemos pronto!",
        "¡Que tengas un buen día!",
        "¡Hasta la próxima!",
        "¡Adiós, amigo!",
    ]
    await ctx.send(random.choice(adios))

@bot.command()
async def mem(ctx):
    images = ['images/mem1.jpg', 'images/mem2.jpg', 'images/mem4.jpg', 'images/mem5.jpg', 'images/mem6.jpg', 'images/mem7.jpg', 'images/mem8.jpg'] 
    with open(random.choice(images), 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
def get_anime_image_url():    
    url = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo'
    res = requests.get(url)
    data = res.json()
    animerandom = random.choice(data['data'])
    return animerandom['attributes']['posterImage']['small']

@bot.command()
async def anime(ctx):
    image_url = get_anime_image_url()
    await ctx.send(image_url)
    

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
bot.run("secret") 
