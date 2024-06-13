from PyroUbot import *

__MODULE__ = "ᴄʀᴇᴀᴛᴇ"
__HELP__ = """
 <b>『 bantuan untuk create 』</b>

<b>• perintah:</b> <code>{0}buat</code> gc namagc
<b>• penjelasan:</b> untuk membuat grup telegram.

<b>• perintah:</b> <code>{0}buat</code> ch namach
<b>• penjelasan:</b> untuk membuat channel telegram.
"""


@PY.UBOT("buat")
async def _(client, message):
    await create_grup(client, message)
