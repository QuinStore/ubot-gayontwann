import asyncio
import random

from PyroUbot.modules import truth_and_dare_string as tod

from PyroUbot import *


@PY.UBOT("apakah")
async def apakah(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("Berikan saya pertanyaan 😐")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.AP)}")


@PY.UBOT("kenapa")
async def kenapa(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("Berikan saya pertanyaan 😐")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.KN)}")


@PY.UBOT("bagaimana")
async def bagaimana(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("Berikan saya pertanyaan 😐")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.BG)}")


@PY.UBOT("dare")
async def dare(client, message):
    try:        
        await message.edit(f"{random.choice(tod.DARE)}")
    except BaseException:
        pass

@PY.UBOT("truth")
async def truth(client, message):
    try:
        await message.edit(f"{random.choice(tod.TRUTH)}")
    except Exception:
        pass


__MODULE__ = "ꜰᴜɴ"
__HELP__ = """
<b>『 truth & dare 』</b>

  <b>• perintah:</b> <code>dare
  <b>• penjelasan:</b> coba aja
  
  <b>• perintah:</b> <code>truth
  <b>• penjelasan:</b> coba aja
  
  <b>• perintah:</b> <code>apakah 
  <b>• penjelasan:</b> coba aja
  
  <b>• perintah:</b> <code>bagaimana 
  <b>• penjelasan:</b> coba aja
  
  <b>• perintah:</b> <code>kenapa
  <b>• penjelasan:</b> coba aja
 
  """
