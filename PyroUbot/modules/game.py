from PyroUbot import *
__MODULE__ = "ɢᴀᴍᴇ"
__HELP__ = """
<b>『 bantuan untuk game 』</b>

  <b>• perintah:</b> <code>{0}catur</code></code>
  <b>• penjelasan:</b> untuk memanggil game catur

  <b>• perintah:</b> <code>{0}game</code></code>
  <b>• penjelasan:</b> untuk memunculkan game random.
  <b>• note : jumlah menu 𝟻𝟶+ game </b>
"""



@PY.UBOT("catur")
async def _(client, message):
    await catur_cmd(client, message)
    

@PY.UBOT("game")
async def _(client, message):
    await game_cmd(client, message)
