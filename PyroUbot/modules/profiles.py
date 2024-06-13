from PyroUbot import *

__MODULE__ = "ᴘʀᴏꜰɪʟᴇ"
__HELP__ = f"""
<b>『 bantuan untuk profile 』</b>

  <b>• perintah:</b> <code>.setbio</code> [text]
  <b>• penjelasan:</b> untuk mengubah bio anda

  <b>• perintah:</b> <code>.setname</code> [text]
  <b>• penjelasan:</b> untuk mengubah nama anda

  <b>• perintah:</b> <code>.block</code> [reply to user]
  <b>• penjelasan:</b> untuk memblokir pengguna

  <b>• perintah:</b> <code>.unblock</code> [reply to user]
  <b>• penjelasan:</b> untuk membuka blokir pengguna
"""


@PY.UBOT("setbio")
async def _(client, message):
    await set_bio(client, message)


@PY.UBOT("setname")
async def _(client, message):
    await setname(client, message)


@PY.UBOT("block")
async def _(client, message):
    await block_user_func(client, message)


@PY.UBOT("unblock")
async def _(client, message):
    await unblock_user_func(client, message)
