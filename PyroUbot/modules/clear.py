from PyroUbot import *
from pyrogram.raw.functions.messages import DeleteHistory
__MODULE__ = "ᴄʟᴇᴀʀ"
__HELP__ = f"""
<b>『 bantuan untuk clear 』</b>

  <b>• perintah:</b> <code>.clear</code>
  <b>• penjelasan:</b> untuk menghapus history
"""


@PY.UBOT("clear")
async def _(client, message):
    user_id = message.chat.id
    bot_info = await client.resolve_peer(user_id)
    await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
