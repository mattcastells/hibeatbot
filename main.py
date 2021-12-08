import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


# EN LA SIGUIENTE LINEA DEBE INTRODUCIRSE EL TOKEN BRINDADO POR LA PLATAFORMA DE DESARROLLO DE DISCORD  - https://discord.com/developers/

client.run(" ")   