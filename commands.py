import discord
from discord.ext import commands
from googlesearch import search

from utils import (
  get_filename, search_file, write_to_file
)

import requests
import os


token = os.environ.get("token")

bot = commands.Bot(command_prefix='!')

@bot.command()
async def google(ctx, *args):
  print("Command: ", args)
  query = ' '.join(args)
  resp = search(query, num=5, tld='co.in', lang='en', stop=5, pause=2)
  for j in resp:
    await ctx.send(j)
  write_to_file(get_filename(ctx.author), query)

@bot.command()
async def recent(ctx, *args):
  print("Search: ", args)
  query = ' '.join(args)
  for data in search_file(get_filename(ctx.author), query):
    await ctx.send(data)

bot.run(token)