from PyroUbot import *

__MODULE__ = "youtube"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʏᴏᴜᴛᴜʙᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}song</code> [sᴏɴɢ ᴛɪᴛʟᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜsɪᴄ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}vsong</code> [sᴏɴɢ ᴛɪᴛʟᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ
"""


@PY.UBOT("vsong")
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song")
async def _(client, message):
    await song_cmd(client, message)
