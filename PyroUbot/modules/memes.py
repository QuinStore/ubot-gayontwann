from PyroUbot import *

__MODULE__ = "memes"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍᴇs 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}memes</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴋᴇʀ ᴍᴇᴍᴇs ʀᴀɴᴅᴏᴍ
"""


@PY.UBOT("memes")
async def _(client, message):
    await memes_cmd(client, message)
