from PyroUbot import *

__MODULE__ = "read"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴏᴄʀ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ocr</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴄᴀ ᴛᴇxᴛ ᴘᴀᴅᴀ ᴍᴇᴅɪᴀ ʏᴀɴɢ ᴅɪ ʀᴇᴘʟʏ
"""


@PY.UBOT("ocr")
async def _(client, message):
    await read_cmd(client, message)
