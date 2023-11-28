from PyroUbot import *

__MODULE__ = "search"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴇᴀʀᴄʜ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}pic</code> [ǫᴜᴇʀʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴘʜᴏᴛᴏ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}gif</code> [ǫᴜᴇʀʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ɢɪꜰᴛ/ᴀɴɪᴍᴀᴛɪᴏɴ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ
"""


@PY.UBOT("pic")
async def _(client, message):
    await pic_bing_cmd(client, message)


@PY.UBOT("bing")
async def _(client, message):
    await pic_bing_cmd(client, message)


@PY.UBOT("gif")
async def _(client, message):
    await gif_cmd(client, message)
