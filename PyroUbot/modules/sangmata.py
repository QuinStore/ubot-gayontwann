from PyroUbot import *

__MODULE__ = "sangmata"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴀɴɢᴍᴀᴛᴀ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}sg</code> [ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴇʀɪᴋsᴀ ʜɪsᴛᴏʀɪ ɴᴀᴍᴀ/ᴜsᴇʀɴᴀᴍᴇ
"""


@PY.UBOT("sg")
async def _(client, message):
    await sg_cmd(client, message)
