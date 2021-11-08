import datetime
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "OTA3MzAzNjAwMTM5Njc3Nzgw.YYlOUw.n6YYL1TRL3UNWao_fe9Ekakb8IA"

client = discord.Client()

prefix = "!"

@client.event
async def on_ready():
    print("logeado")


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    userMessage = str(message.content).lower()
    channel = str(message.channel.name)
    if message.author == client.user:
        return

    userMessage = userMessage.lower()

    if userMessage == prefix + "contract":
        embed_contract = discord.Embed(title="🧾**CONTRATOS**", description=":pushpin: TOKEN: https://bscscan.com/token/0xa1e34c4d25de38f0491f8b7b279c254f45e7d8e3\n\n"
                                                                            ":pushpin: NFTs: https://bscscan.com/token/0x9e3a158a357a6403aad454f501d69e86b04a2174", timestamp=datetime.datetime.utcnow())
        await message.channel.send(embed=embed_contract)

    elif userMessage == prefix + "redes" or userMessage == prefix + "social":
        embed_redes = discord.Embed(title="**REDES SOCIALES**",
                                       description="Twitter : https://twitter.com/predatorprogame?s=21\n"
                                                   "YouTube : https://youtube.com/channel/UCtanZ2hYPOBl1OOmNZkrPXQ\n"
                                                   "Telegram Anuncios en español: https://t.me/PredatorNoticias\n"
                                                   "Telegram Comunidad en español: https://t.me/predator_pro_es\n"
                                                   "Telegram Comunidad en Ingles: https://t.me/predator_pro",
                                       timestamp=datetime.datetime.utcnow())
        await message.channel.send(embed = embed_redes)
    elif userMessage == prefix + "download" or userMessage == prefix + "descargas":
        await message.channel.send("**PAGINA DE DESCARGA**\n\n"
                                    "https://predator-game.com/dashboard/download/")
    elif userMessage == prefix + "roi":
        await message.channel.send("**ROI DE PREDATORS**\n\n"
                                   "Video Explicativo: https://youtu.be/YOfqa7m4-IQ")

    elif userMessage == prefix + "web" or userMessage == prefix + "page" or userMessage == prefix + "webpage":
        await message.channel.send("**Pagina Web**\n"
                                   "https://predator-game.com/")
    elif userMessage == prefix + "help":
        embed_help = discord.Embed(title="🧾**COMANDOS**",
                                       description="!web\n"
                                                    "!roi\n"
                                                    "!download\n"
                                                    "!redes\n"
                                                    "!contract",
                                       timestamp=datetime.datetime.utcnow())
        await message.channel.send(embed = embed_help)


client.run(TOKEN)
