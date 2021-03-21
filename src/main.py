# python3 -m pip install -U discord.py
# pip install requests

import sys
import time
import discord
import requests
import json
import conoha_wrap
import conoha_main
import conoha_sub
import utility
from config import *


client = discord.Client()
client.isProcessing = False

# 起動時
@client.event
async def on_ready():
  print('discord login')

# メッセージ受信時
@client.event
async def on_message(_message):
  if _message.author.bot or not(_message.channel.name in DISCORD_CHANNEL_NAMES):
    return

  channel = _message.channel

  if _message.content in utility.full_commands('open'):
    if client.isProcessing:
      await utility.post_embed_failed(channel, f"You can only run one at a time.\nCanceled: {utility.full_commands('open')}")
      return None
    client.isProcessing = True
    await conoha_main.create_vm_from_image(channel)
    client.isProcessing = False

  if _message.content in utility.full_commands('close'):
    if client.isProcessing:
      await utility.post_embed_failed(channel, f"You can only run one at a time.\nCanceled: {utility.full_commands('close')}")
      return None
    client.isProcessing = True
    await conoha_main.create_image_from_vm(channel)
    client.isProcessing = False

  if _message.content in utility.full_commands('help'):
    await utility.post_asagao_minecraft_commands(channel)

  if _message.content in utility.full_commands('plan'):
    await conoha_sub.post_discord_conoha_vm_plans(channel)

  if _message.content in utility.full_commands(['myid', 'userid']):
    await utility.post_user_id(_message)

  if _message.content in utility.full_commands('version'):
    await utility.post_version(channel)


client.run(DISCORD_TOKEN)
