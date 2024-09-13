import discord
import json
import os
import random
from keep_alive import keep_alive
import requests
from replit import db

# Enable intents for the bot
intents = discord.Intents.default()
intents.messages = True  # Allow the bot to receive message events

client = discord.Client(intents=intents)
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person / bot!"]

if "responding" not in db:
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "-" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
  
    if msg.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)

    if db["responding"]:
      options = starter_encouragements
      if "encouragements" in db:
        options = options + list(db["encouragements"])
  
      if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
      encouraging_message = msg.split("$new ",1)[1]
      update_encouragements(encouraging_message)
      await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
      encouragements = []
      if "encouragements" in db:
        index = int(msg.split("$del",1)[1])
        delete_encouragement(index)
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)

    if msg.startswith("$list"):
      encouragements = []
      if "encouragements" in db:
        encouragements = db["encouragements"]
      await message.channel.send(list(encouragements))

    if msg.startswith("$responding"):
      value = msg.split("$responding ",1)[1]
      if value.lower() == "true":
        db["responding"] = True
        await message.channel.send("Responding is on.")
      else:
        db["responding"] = False
        await message.channel.send("Responding is off.")

def update_encouragements(encouraging_msg):
  if "encouragements" in db:
    encouragements = db["encouragements"]
    encouragements.append(encouraging_msg)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_msg]

def delete_encouragement(index):
  encouragements= db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

# Get the bot token from the environment
token = os.environ['TOKEN']
if token:
    print(f'Token: {token[:5]}...')  # For security, only print part of the token
    keep_alive()
    client.run(token)
else:
    print('Token not found in environment variables.')
