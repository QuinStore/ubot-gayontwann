from PyroUbot import *

__MODULE__ = "nulis"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴᴜʟɪs 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}nulis</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ɴᴜʟɪs sᴇsᴜᴀᴛᴜ ᴋᴀʟɪᴍᴀᴛ/ᴋᴀᴛᴀ ᴅɪ ʙᴜᴋᴜ
"""


@PY.UBOT("nulis")
async def _(client, message):
    await nulis_cmd(client, message)
