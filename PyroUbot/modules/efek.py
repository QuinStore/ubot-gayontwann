from PyroUbot import *

__MODULE__ = "ᴇꜰᴇᴄᴛ"
__HELP__ = f"""
<b>『 bantuan untuk efect 』</b>

  <b>• perintah:</b> <code>.efect</code> [efek_code - reply to voice note]
  <b>• penjelasan:</b> untuk mengubah suara voice note

  <b>• perintah:</b> <code>.listefect</code>
  <b>• penjelasan:</b> untuk melihat daftar efect

"""


@PY.UBOT("efect")
async def _(client, message):
    await convert_efek(client, message)


@PY.UBOT("listefect")
async def _(client, message):
    await list_cmd_efek(client, message)


