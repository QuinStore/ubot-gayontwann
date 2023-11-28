from PyroUbot import *

__MODULE__ = "telegraph"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇʟᴇɢʀᴀᴘʜ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tg</code> [ʀᴇᴘʟʏ ᴍᴇᴅɪᴀ/ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ/ᴛᴇxᴛ ᴋᴇ telegra.ph
"""


@PY.UBOT("tg")
async def _(client, message):
    await tg_cmd(client, message)
