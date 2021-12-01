import datetime
from io import BytesIO
import discord
from discord.ext import commands
from dotenv import load_dotenv
from PIL import Image, ImageChops, ImageDraw, ImageFont

load_dotenv()
TOKEN = "OTA3MzAzNjAwMTM5Njc3Nzgw.YYlOUw.n6YYL1TRL3UNWao_fe9Ekakb8IA"

client = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents().all())


def circle(pfp, size=(215, 215)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")

    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp


@client.event
async def on_ready():
    print("Bot Activo")


@client.command()
async def contract(ctx):
    embed_contract = discord.Embed(title="🧾**CONTRATOS**",
                                   description=":pushpin: TOKEN: https://bscscan.com/token/0xa1e34c4d25de38f0491f8b7b279c254f45e7d8e3\n\n"
                                               ":pushpin: NFTs: https://bscscan.com/token/0x9e3a158a357a6403aad454f501d69e86b04a2174",
                                   timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed_contract)


@client.command()
async def redes(ctx):
    embed_redes = discord.Embed(title="**REDES SOCIALES**",
                                description="Twitter : https://twitter.com/predatorprogame?s=21\n"
                                            "YouTube : https://youtube.com/channel/UCtanZ2hYPOBl1OOmNZkrPXQ\n"
                                            "Telegram Anuncios en español: https://t.me/PredatorNoticias\n"
                                            "Telegram Comunidad en español: https://t.me/predator_pro_es\n"
                                            "Telegram Comunidad en Ingles: https://t.me/predator_pro",
                                timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed_redes)


@client.command()
async def download(ctx):
    await ctx.send("**PAGINA DE DESCARGA**\n\n"
                   "https://predator-game.com/dashboard/download/")


@client.command()
async def roi(ctx):
    await ctx.send("**ROI DE PREDATORS**\n\n"
                   "Video Explicativo: https://youtu.be/YOfqa7m4-IQ")


@client.command()
async def web(ctx):
    await ctx.send("**Pagina Web**\n"
                   "https://predator-game.com/")


@client.command()
async def bug(ctx):
    embed_bug = discord.Embed(title="🧾**¿HAS REPORTADO UN BUG Y SE PIERDE ENTRE MENSAJES?**",
                                   description="— Hemos creado un formulario de reporte de bugs SOBRE EL JUEGO.\n\n"
                                               "Si has encontrado uno, por favor, utiliza este enlace para hacerlo saber y solucionarlo.\n\n"
                                               ":pushpin: https://forms.gle/z3bFXWyTPBYBuutX6",
                                   timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed_bug)


@client.command()
async def b(ctx):
    embed_b = discord.Embed(title=":rocket: BOT PRO :rocket:",
                                   description=":warning: Recuerden que pueden utilizar el comando **!help** para usar nuestro BOT de consultas básicas.:fire:",
                                   timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed_b)


@client.command(name="help")
async def help(ctx):
    embed_help = discord.Embed(title="🧾**COMANDOS**",
                               description="!web >>> Muestra la página oficial de Predator\n"
                                           "!roi >>> Muestra un video explicativo del ROI\n"
                                           "!download >>> Muestra la página oficial de descarga de Predator\n"
                                           "!redes >>> Muestra las redes oficiales de Predator\n"
                                           "!contract >>> Muestra los contratos de Predator\n"
                                           "!bug>>> Muestra el formulario para reportar los bugs!\n"
                                           "!faq>>> Muestra las preguntas más frecuentes!\n"
                                           "!pro >>> Muestra el precio del token\n"
                                           "!whitepaper >>> Muestra los Whitepapers en Español e Ingles",
                               timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed_help)

    
@client.command()
async def whitepaper(ctx):
    embed_whitepaper = discord.Embed(title=":map: WHITEPAPER Y ROADMAP ACTUALIZADO :map:",
                               description="— Luego de semanas preparando todo y algunos últimos ajustes, ya fue hecho público el nuevo whitepaper y el roadmap actualizado del proyecto.\n\n"
                                           ":warning: Los enlaces al whitepaper en inglés y español son los siguientes:\n\n"
                                           ":flag_us: WHITEPAPER EN INGLÉS : https://docs.predator-game.com/welcome-to-predator/introduction\n"
                                           ":flag_es: WHITEPAPER EN ESPAÑOL: https://spdocs.predator-game.com/bienvenido-a-predator/master\n\n"
                                           "El roadmap nuevo lo pueden ver en la web o en el whitepaper.\n\n"
                                           ":rotating_light:Se debe mencionar que el documento tendrá cambios a futuro: más información que no haya sido añadida aún o futuras implementaciones no mencionadas.\n"
                                           "Buen juego para todos :heart:",
                               timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed_whitepaper)

@client.event
async def on_member_join(member):
    card = Image.open("card.png")

    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = circle(pfp, (215, 215))
    card.paste(pfp, (425, 80))

    draw = ImageDraw.Draw(card)
    name = str(f"Bienvenido, {member.display_name}!")
    relleno = "Te uniste a la comunidad de predator!"
    font = ImageFont.truetype("Montserrat-MediumItalic.ttf", 30)
    draw.text((375, 330), name, font=font, fill="white")
    draw.text((255, 380), relleno, font=font, fill="white")
    card.save("profile.png")
    await client.get_channel(888133258490040381).send(file=discord.File("profile.png"))
    await client.get_channel(888133258490040381).send("Ve al canal **#pick-your-lenguage** para seleccionar tu idioma!\n\n"
                                                      "Go to **#pick-your-lenguage** to select a language!")
    
    
    
@client.command()
async def faq(ctx):
    embed_faq = discord.Embed(title="   PREDATOR GAME ($PRO)\n  :warning:FAQ — Preguntas Frecuentes ",
                               description=":arrow_forward:¿QUE NECESITO PARA COMENZAR A JUGAR?\n  "
                                           "R: Necesitas un NFT y al menos 50 $PRO para hacer las misiones diarias.\n \n "
                                           ":arrow_forward:¿DONDE PUEDO REGISTRARME?\n"
                                           "R: https://predator-game.com/market/#/auth/register\n\n"
                                           ":arrow_forward:¿CUÁNTO VALEN LOS NFTs?\n"
                                           "R: Están disponibles desde los 0.14 BNB a 1.1 BNB, también eventualmente hay cápsulas por minteo, con un valor de US$100 en $PRO (Cantidad definida por el Oráculo).\n\n"
                                           ":arrow_forward:¿COMO ACCEDO AL MARKET?\n"
                                           "R: https://predator-game.com/market/#/\n\n"
                                           ":arrow_forward:¿DE CUÁNTO TIEMPO ES EL ROI?\n"
                                           "R: Se estiman unos 30 a 45 días dependiendo de tu inversión inicial.\n\n"
                                           ":arrow_forward:¿CUÁNTO SE GANARÁ EN EL JUEGO?\n"
                                           "R: Las ganancias están entre 4 a 15 dólares diarios, variando según cuantos $PRO deposites dentro del juego y de tu desempeño y nivel a la hora de completar misiones.Puedes ganar más, pero tendrás que apostar y arriesgar a perder más dinero. También puedes ganar dinero con el farming, cada 7, 14 o 30 días según los stats de tu NFT.\n\n"
                                           ":arrow_forward:¿HAY FARMING?\n"
                                           "R: Sí, el apartado de farming se encuentra en nuestra web.\n\n"
                                           ":arrow_forward:¿HABRÁ STAKING?\n"
                                           "R: Sí, se está desarrollando un sistema de staking que beneficia a los top holders.\n\n"
                                           ":arrow_forward:¿PODRÉ COMPRAR NFTs CON PRO?\n"
                                           "R: Actualmente puedes comprar NFT en PRO usando el sistema de cápsulas.\n\n"
                                           ":arrow_forward:¿PARA QUÉ SE USARÁ EL PRO?\n"
                                           "R: Para compra de NFT, powerups (por partida), armas, objetos de un solo uso, apuestas, torneos, staking, farming.\n\n"
                                           ":arrow_forward:¿PARA QUE SE UTILIZARA EL TOR?\n"
                                           "R: Para compra de NFT, skins únicos, power ups (de tiempo), apuestas. Se recibirán recompensas en TOR.\n"
                                           ":arrow_forward:¿HAY UN SISTEMA DE ORÁCULO?\n"
                                           "R: Si hay un sistema económico basado en oráculo.\n\n"
                                           ":arrow_forward:¿COMO TRANSFORMO MIS PRO A PS (Pro silver)?\n"
                                           "R: Debes apretar en el botón 'swap' dentro del juego e intercambiarlo. Recuerda que 1 $PRO=1000 PS.\n\n "
                                           ":arrow_forward:¿QUE ES $TOR?\n"
                                           "R: $TOR sera nuestro token secundario, que se usará principalmente para pagar las recompensas dentro del juego.\n\n"
                                           ":arrow_forward:¿VAMOS A RETIRAR EN $TOR O EN $PRO?\n"
                                           "R: Puedes retirar los dos simultáneamente sin ningún problema.\n\n"
                                           ":arrow_forward:¿QUE PASARA CON EL TOKEN $PRO?\n"
                                           "R: $PRO será nuestro token de gobernanza, es decir, de inversión y gasto.\n\n"
                                           ":arrow_forward:¿EL RETIRO DE MIS TOKENS SERA SOLO UNA VEZ POR MES?\n"
                                           "R: No. Puedes retirar cuando lo desees eligiendo tu tiempo y comision de retiro.\n\n"
                                           ":arrow_forward:¿HAY SISTEMA DE BECAS?\n"
                                           "R: Si. El sistema de becas se encuentra en etapa de desarrollo.\n\n"
                                           ":arrow_forward:¿EL MODO ESPECTADOR YA ESTA HABILITADO?\n"
                                           "R: El modo espectador se encuentra en testeos internos.\n\n"
                                           ":arrow_forward:¿CUANDO ES LA PREVENTA DEL TOKEN $TOR?\n"
                                           "R: La fecha de la preventa sera anunciada en los próximos dias.\n\n"
                                           ":arrow_forward:¿DONDE PUEDO ENCONTRAR EL WHITEPAPER?\n"
                                           "R: Puedes encontrarlo en nuestra web o siguiendo el siguiente link: https://docs.predator-game.com/welcome-to-predator/introduction",
                               timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed_faq)

client.run(TOKEN)
