import discord.py
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv('BOT_TOKEN')

client = commands.Bot(command_prefix='-', intends=discord.Intends.all())

@client.event
async def on_ready():
  print('Yoooo!! Successful Bot Logined')
  print('Bot Name : {client.user.name}')
  print('Bot Id : {client.user.id}')

@client.command()
async def ping(ctx):
  await ctx.send("Pong!")

client.run(TOKEN)
