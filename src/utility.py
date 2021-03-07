import sys
import time
import asyncio
import discord
import requests
import json
from config import *


def full_commands(_commands2):
  if type(_commands2) == str:
    _commands2 = [_commands2]
  elif type(_commands2) == int or type(_commands2) == float:
    _commands2 = [str(_commands2)]
  command1 = ['/mc', '/minecraft']
  return [f'{c1} {c2}' for c1 in command1 for c2 in _commands2] # ex: ['/mc open', '/minecraft open']


def parse_json(_json):
  _json = json.loads(_json)
  _json = json.dumps(_json, indent=2)
  print(_json)
  return _json


async def post_embed(_message, _title='', _content='', _color=discord.Color.default):
  embed = discord.Embed(title=_title,description=_content, color=_color)
  await _message.channel.send(embed=embed)


async def post_embed_complite(_message, _title, _content):
  _content = _content + '\ndone.'
  await post_embed(_message, _title=_title, _content=_content, _color=discord.Color.green())


async def post_embed_failed(_message, _content):
  _content = _content + '\nPlease try again or contact admin user.\n\
    Please remove unnecessary vm server or image.'
  await post_embed(_message, _title='Failed', _content=_content, _color=discord.Color.gold())


async def post_embed_error(_message, _content):
  _content = _content + f'\n\
    Stop asagao-minecraft server.\n\
    Can not run all commands.\n\
    Please contact admin user.\n\
    {ADMIN_USER_ID}'
  await post_embed(_message, _title='Error', _content=_content, _color=discord.Color.red())


async def post_user_id(_message):
  await post_embed_complite(_message, 'user id', str(_message.author.id))


async def post_asagao_minecraft_commands(_message):
  content = f"\
    > Create VM from image, for play minecraft.\n\
    > {str(full_commands('open'))}\n\
    \n\
    > Delete VM and save image, finished play minecraft.\n\
    > {str(full_commands('close'))}\n\
    \n\
    > help.\n\
    > {str(full_commands('help'))}\n\
    \n\
    > ConoHa vm plans list.\n\
    > {str(full_commands('plan'))}\n\
    \n\
    > user id.\n\
    > {str(full_commands(['myid', 'userid']))}\n\
    \n\
  "
  await post_embed_complite(_message, 'asagao-minecraft commands', content)
