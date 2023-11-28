from PyroUbot import *

__MODULE__ = "limit"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟɪᴍɪᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}limit</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴄᴇᴋ sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴀᴘᴀᴋᴀʜ ᴛᴇʀᴋᴇɴᴀʟ ʟɪᴍɪᴛ ᴀᴛᴀᴜ ᴛɪᴅᴀᴋ
"""

@ubot.on_message(filters.command("limit", "$") & filters.user(SUDO_USERS))
@PY.UBOT("limit")
async def _(client, message):
    await limit_cmd(client, message)
