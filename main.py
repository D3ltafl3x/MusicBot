import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)



client.run("OTYwNjY3OTkwNzEyNTIwODA1.YktxyQ.Ff-u3N-0vUf8ebDJD0hQ_0k0Eks")