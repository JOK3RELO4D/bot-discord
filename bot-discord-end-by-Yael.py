import os
import requests 
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Saludos, soy una eminencia. Descubre la oscuridad por ti mismo, {bot.user}. ¡Bienvenido al servidor! 🌑🔮")
    
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
        "$fondo: Proporciona imagenes funcionales de fondo de pantalla",
        "$tokio: Recomienda animes e imagenes random",
        "$mem: Genera fotos de memes de acuerdo a la programacion",
        "$duck: Genera imagenes de patos, adorable, no lo crees?",
        "$adios: Ofrece una despedida diferente",
        "$naturaleza: Ofrece una lista de naturaleza",
        "$python: Envia codigos utilizables basicos",
        "$videojuegos: Seccion acerca de los videojuegos",
        "$fox: Seccion acerca de los zorros",
        "$dog: Seccion que envia imagenes de dog",
        "$contaminacion: El usuario podra interactuar con la ecologia,
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
async def tokio(ctx):
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

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)
    
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def fondo(ctx):
    imagenes = [f for f in os.listdir('fondos') if os.path.isfile(os.path.join('fondos', f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    imagen = random.choice(imagenes)
    await ctx.send(file=discord.File(os.path.join('fondos', imagen)))
    
    
@bot.command()
async def creator(ctx):
    funciones = [
        ("on_ready", "Se ejecuta cuando el bot se ha conectado correctamente a Discord."),
        ("hello", "Saluda al usuario."),
        ("bye", "Se despide del usuario."),
        ("heh", "Repite la palabra 'he' varias veces."),
        ("admin", "Permite al bot enviar un mensaje en nombre del usuario y borra el mensaje original."),
        ("repetir", "Repite un mensaje."),
        ("reglas", "Muestra las reglas del servidor."),
        ("borrar", "Borra mensajes en el canal."),
        ("helplease", "Muestra una lista de comandos disponibles."),
        ("mensaje", "Envía un saludo aleatorio."),
        ("adios", "Se despide de manera aleatoria."),
        ("mem", "Envía una imagen de meme aleatoria."),
        ("tokio", "Recomienda un anime de Tokio."),
        ("duck", "Envía una imagen aleatoria de un pato."),
        ("fox", "Envía una imagen aleatoria de un zorro."),
        ("dog", "Envía una imagen aleatoria de un perro."),
        ("fondo", "Envía una imagen de fondo de pantalla aleatoria.")
    ]
    mensaje = "Funciones utilizadas por el creador:\n\n" + "\n".join([f"{funcion}: {descripcion}" for funcion, descripcion in funciones])
    await ctx.send(mensaje)
    
    
    
@bot.command()
async def naturaleza(ctx):
    naturaleza = [
        "$historias: Sumérgete en la historia de la naturaleza y la Tierra.",
        "$curiosidades: Descubre datos curiosos sobre el mundo natural.",
    ]
    
    Naturaleza = "Comandos relacionados con la naturaleza:\n\n" + "\n".join(naturaleza)
    await ctx.send(Naturaleza)
    
@bot.command()
async def curiosidades(ctx):
    curiosidades = [
        "1. Árboles y sus características:",
        "Los árboles son seres vivos que forman parte del Reino Plantae.",
        "Tienen un tronco lignificado o leñoso, más duro y grueso que los arbustos.",
        "2. Tipos de árboles:",
        "Árboles de hoja caduca: Pierden sus hojas en otoño.",
        "Árboles de hoja perenne: Mantienen sus hojas durante todo el año.",
        "3.Partes de un árbol:",
        "Raíces: Absorben agua y nutrientes del suelo.",
        "Tronco: Soporte principal del árbol.",
        "Ramas y hojas: Realizan la fotosíntesis y producen oxígeno.",
    ]
    
    arbol = "Información sobre plantas y árboles:\n\n" + "\n".join(curiosidades)
    await ctx.send(arbol)
    
@bot.command()
async def historias(ctx):

    historianatural = [
    "Plinio el Viejo y la Naturalis Historia:",
    "Plinio el Viejo escribió Naturalis Historia en el año 77 d.C.",
    "Esta obra abarcaba zoología, botánica, agricultura, mineralogía, medicina y magia.",
    "La Tierra y su historia:",
    "La Tierra es el quinto mayor planeta del sistema solar y el único lugar donde existe vida.",
    "Los patrones climáticos varían desde los polos hasta las zonas ecuatoriales.",
    "La evolución de la historia natural:",
    "Desde los antiguos griegos hasta los naturalistas del siglo XVIII.",
    "El concepto de historia natural incluye minerales, vegetales, animales y procesos geológicos.",
    ]

    listahistoria = "Información sobre plantas y árboles:\n\n" + "\n".join(historianatural)
    await ctx.send(listahistoria)

    


@bot.command()
async def videojuegos(ctx):
    lista_videojuegos = [
        "$recomendar: Sugiere títulos de videojuegos populares.",
        "$personajes: Describe a tus personajes favoritos de videojuegos.",
        "$historia: Sumérgete en la historia de los videojuegos.",
        "$curiosidades: Descubre datos interesantes sobre la cultura gamer.",
    ]
    
    videojuegos = "Comandos relacionados con videojuegos:\n\n" + "\n".join(lista_videojuegos)
    await ctx.send(videojuegos)
    
@bot.command()
async def recomendar(ctx):
    recomendaciones = [
        "Apex Legends: Genero: Battle Royale.",
        "Dark Souls: Genero: Aventura, RPG.",
        "Stardew Valley: Genero: Simulacion, RPG.",
        "Celeste: Genero: Plataformas, aventura.",
        "Hollow Knight: Aventura, accion.",
    ]
    recomendar= "Comandos relacionados con videojuegos:\n\n" + "\n".join(recomendaciones)
    await ctx.send(recomendar)
    
@bot.command()
async def historia(ctx):
    history = [
        "1.Pong (1972): Uno de los primeros videojuegos comerciales, creado por Atari.",
        "2.Space Invaders(1978): Revolucionó los juegos de disparos y marcó el inicio de la era de las máquinas arcade.",
        "3.Pac-Man(1980): El icónico comecocos amarillo que se convirtió en un fenómeno cultural.",
        "4.Donkey Kong(1981): Introdujo a Mario (entonces llamado Jumpman) y sentó las bases para los juegos de plataformas.",
        "5.Tetris(1984): El adictivo juego de bloques que se ha adaptado a casi todas las plataformas imaginables.",
        "6.Super Mario Bros. (1985): El juego que catapultó a Mario a la fama y definió los juegos de plataformas.",
        "7.The Legend of Zelda (1986): La primera entrega de la épica saga de aventuras de Link y Zelda.",
        "8.Sonic the Hedgehog (1991): El veloz erizo azul de SEGA que compitió con Mario.",
        "9.Street Fighter II (1991): Popularizó los juegos de lucha y presentó personajes como Ryu y Chun-Li.",
        "10.Doom (1993): Pionero en los juegos de disparos en primera persona y precursor de los juegos de acción 3D.",
    ]
    
    history1= "Interesante, lo que solemos jugar ahora:\n\n" + "\n".join(history)
    await ctx.send(history1)
    
@bot.command()
async def personajes(ctx):
    personaje = [
        "Samus Aran.",
        "PAC-MAN",
        "Kratos.",
        "Mario.",
        "Cloud Strife.",
        "Solid Snake",
    ]
    person= "Mejores personajes ranking:\n\n" + "\n".join(personaje)
    await ctx.send(person)
    
@bot.command()
async def curiosidades0(ctx):
    curiosidad = [
        "Spacewar, creado en tan solo 200 horas en 1961, fue el primer videojuego en el que se podía disparar.",
        "Call of Duty: Modern Warfare 2 obtuvo la mayor recaudación en su primer día de lanzamiento, con 410 millones de dólares.",
        "En 2019, se determinó que existían poco más de un millón de videojuegos en total.",
        "La máquina recreativa más grande tiene dimensiones de más de 4 metros de alto y casi 2 metros de ancho.",
        "El primer trabajo en el que vimos a Mario no fue como fontanero, sino como carpintero en el juego Donkey Kong.",
        "Se dice que existe un juego arcade llamado Polybius que es extremadamente misterioso. No se conserva ninguna copia de él, y se rumorea que causaba efectos extraños en quienes lo jugaban.",
    ]
    mensaje = "Curiosidades:\n\n" + "\n".join(curiosidad)
    await ctx.send(mensaje)
    

@bot.command()
async def python(ctx):
    lista_python = [
        "pip: Instala paquetes de software desde el índice de paquetes de Python.",
        "print: Muestra un mensaje en la pantalla o en otro dispositivo de salida estándar.",
        "type: Verifica el tipo o clase de un objeto.",
        "range: Genera una secuencia de enteros desde 0 hasta n (no incluido).",
        "len: Devuelve la longitud (cantidad de elementos) de un objeto.",
        "input: Lee una línea de entrada desde el usuario.",
        "for: Crea un bucle for para iterar sobre una secuencia.",
        "while: Crea un bucle while que se ejecuta mientras se cumple una condición.",
        "if: Realiza una comprobación condicional.",
        "def: Define una función.",
        "import: Importa un módulo o paquete.",
        "exit: Sale del programa.",
    ]
    
    python = "Si inicias en el mundo de la programacion estos comandos te seran de gran ayuda:\n\n" + "\n".join(lista_python)
    await ctx.send(python)
    
@bot.command()
async def contaminacion(ctx):
    contaminar = [
        "En esta seccion encontraras relacion de la actividad humana hacia el mundo natural ",
        "$impacto: Sumérgete en la historia de la naturaleza y la Tierra.",
        "$datos: Descubre datos curiosos sobre el mundo natural.",
        "$origen: Descubre la historia de la degradacion de el mundo natural.",
        "$soluciones: Descubre datos curiosos sobre el mundo natural.",
        "$huella: Descubre tu huella de carbono",
        "$contaminacionimages: Descubre los grandes problemas de la contaminacion con imagenes"
        "$importancia: La concientizacion es la forma mas eficiente de erradicar la contaminacion"
    ]
    await ctx.send("\n".join(contaminar))
    
@bot.command()
async def impacto(ctx):
    impacto1 = [
        "Impacto global : La Organización Mundial de la Salud (OMS) estima que la contaminación del aire es responsable a nivel mundial de 1.4% de las muertes y del 0.8% de los años de vida",
        "Impacto del aire: Se asocia con un aumento del dioxido de carbono, por ello la exposicion a este se vuelve mortal",
        "Impacto a la distribucion: Es el repentino aumento de contaminantes de acuerdo a la division demografica y la creciente expansion de este conflicto",
        "Impacto en el nacimiento: En el nacimiento existen diversas problematicas que provocan el avance de la contaminacion asi como los altos niveles de sobrepoblacion que se pueden presentar.",
        "Si quieres saber mas sobre el impacto del agua puedes acceder a ello con el mensaje $impactoagua y acceder al impacto de la tierra con $mensajetier"
    ]
    await ctx.send("\n".join(impacto1))
    
@bot.command()
async def datos(ctx):
    datos1 = [
        "Se estima que 9 de cada 10 personas en el mundo respiran aire contaminado. ",
        "La contaminacion del suelo afecta la calidad de los alimentos y el agua.",
        "La produccion de carne contribuye a la contaminación del agua y la deforestación",
        "$La contaminacion apoya a la degradacion de el mundo natural.",
        "$La contaminacion es un 90% causada por los humanos",
    ]
    await ctx.send("\n".join(datos1))
    

@bot.command()
async def origen(ctx):
    origen1 = [
        "Luces de seguridad y publicidad.",
        "Quema de combustibles fósiles, como carbon, petroleo y gas natural.",
        "La produccion de carne contribuye a la contaminación del agua y la deforestacion",
        "La contaminacion causada por la creacion de automoviles y medios de transporte.",
        "Se cree que la contaminacion puede estar originada en los inicios de la revolucion industrial",
    ]
    await ctx.send("\n".join(origen1))
    
@bot.command()
async def soluciones(ctx):
    datos1 = [
        "Proteccion del espacio animal ",
        "Gestion adecuada de servicios.",
        "Control de industrias u espacios que generen grandes cantidades de dioxido de carbono",
        "Promover energias naturales.",
        "Utilizacion de paneles solares que contribuyan a la eficiencia energetica y apoye a la ecologia",
    ]
    await ctx.send("\n".join(soluciones))
    
@bot.command()
async def huella(ctx):
    huella1 = [
        "Haz clic en este link para saber mas:",
        "https://calculadora-carbono.climatehero.org/?source=MicrosoftKeywordsLatin&msclkid=d3d6a7c282f917a54f6ec1c9e74a20f8",
    ]
    await ctx.send("\n".join(huella1))
    

@bot.command()
async def importancia(ctx):
    importance = [
        "Proteger la salud: La contaminación del aire, el agua y el suelo puede tener efectos graves en la salud humana, incluyendo enfermedades respiratorias, cáncer y problemas de salud mental.",
        "Conservar la biodiversidad: La contaminación puede afectar a los ecosistemas naturales y la biodiversidad, poniendo en peligro a muchas especies de plantas y animales.",
        "Preservar los recursos naturales: La contaminación puede agotar los recursos naturales como el agua dulce y el suelo fértil, lo que afecta la disponibilidad de alimentos y agua potable.",
        "Reducir el impacto del cambio climático: Al reducir la contaminación, podemos disminuir las emisiones de gases de efecto invernadero y mitigar el cambio climático.",
        "Promover la sostenibilidad: Abordar la contaminación es esencial para promover un estilo de vida sostenible y asegurar un futuro saludable para las generaciones futuras.",
    ]    
    await ctx.send("\n".join(importance))
    

@bot.command()
async def chau(ctx):
    byexd = [
        "¡Hasta luego!",
        "¡Adiós!",
        "¡Nos vemos pronto!",
        "¡Que tengas un buen día!",
        "¡Hasta la próxima!",
        "¡Adiós, amigo!",
    ]
    await ctx.send(random.choice(byexd))
    
@bot.command()
async def impactoagua(ctx):
    impacto_agua1 = [
        "Impacto en los oceanos: El vertido de productos químicos, desechos industriales y aguas residuales al mar provoca la contaminación del agua y afecta gravemente a los ecosistemas marinos.",
        "Impacto en los rios: La contaminación de los ríos con productos químicos, desechos industriales y aguas residuales afecta a la vida acuática y puede tener efectos nocivos en la salud humana.",
        "Impacto en los lagos: La contaminación de los lagos con nutrientes y productos químicos puede provocar la proliferación de algas y la muerte de peces, afectando a los ecosistemas acuáticos.",
    ]
    await ctx.send("\n".join(impacto_agua1))

@bot.command()
async def impactotier(ctx):
    impacto_tier = [
        "Impacto en el suelo: La contaminación del suelo con productos químicos, desechos industriales y residuos agrícolas puede afectar a la fertilidad del suelo y a la salud de las plantas y animales.",
        "Impacto en la agricultura: La contaminación del suelo puede afectar a los cultivos y a la calidad de los alimentos, lo que puede tener efectos negativos en la salud humana.",
        "Impacto en los ecosistemas terrestres: La contaminación del suelo puede tener efectos nocivos en los ecosistemas terrestres y en la biodiversidad.",
    ]
    await ctx.send("\n".join(impacto_tier))
    
    
bot.run("AQUI VA EL TOKEN") 
