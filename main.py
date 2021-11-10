import datetime
from io import BytesIO
import discord
from discord.ext import commands
from dotenv import load_dotenv
from PIL import Image, ImageChops, ImageDraw, ImageFont

load_dotenv()
TOKEN = "OTA1MjA4MDA5NDkwMzE3Mzky.YYGupw.tEM1RA3cccCNvLrd7JsAmoZewWI"

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


@client.command(name="help")
async def help(ctx):
    embed_help = discord.Embed(title="🧾**COMANDOS**",
                               description="!web >>> Muestra la página oficial de Predator\n"
                                           "!roi >>> Muestra un video explicativo del ROI\n"
                                           "!download >>> Muestra la página oficial de descarga de Predator\n"
                                           "!redes >>> Muestra las redes oficiales de Predator\n"
                                           "!contract >>> Muestra los contratos de Predator",
                               timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed_help)


@client.event
async def on_member_join(member):
    card = Image.open("card.png")

    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = circle(pfp, (215, 215))
    card.paste(pfp, (425, 80))

    draw = ImageDraw.Draw(card)
    name = str(f"Bienvenido, {member.display_name}")
    relleno = "Dirigete a #language-idioma"
    font = ImageFont.truetype("Montserrat-MediumItalic.ttf", 30)
    draw.text((365, 330), name, font=font, fill="white")
    draw.text((300, 380), relleno, font=font, fill="white")
    card.save("profile.png")
    await client.get_channel(888133258490040381).send(file=discord.File("profile.png"))
    

client.run(TOKEN)
