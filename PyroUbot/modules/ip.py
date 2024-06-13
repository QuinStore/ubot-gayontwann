from PyroUbot import *


__MODULE__ = "ip"
__HELP__ = f"""
<b>『 bantuan untuk ipinfo 』</b>

  <b>• perintah:</b> <code>.ipinfo</code> [ip addreꜱ]
  <b>• penjelasan:</b> untuk mendapatkan informasi ip addres 
  """


@PY.UBOT("ipinfo")
async def _(client, message):
    await hacker_lacak_target(client, message)
