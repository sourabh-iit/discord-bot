import discord
import os

token = os.environ.get("token")

client = discord.Client()

@client.event
async def on_message(message):
  if message.content.lower()=="hi":
    await message.channel.send("hey")

client.run(token)