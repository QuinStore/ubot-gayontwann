from PyroUbot import *

__MODULE__ = "spam"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴀᴍ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}spam</code> [ᴊᴜᴍʟᴀʜ_ᴘᴇsᴀɴ - ᴘᴇsᴀɴ_sᴘᴀᴍ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ sᴘᴀᴍ ᴘᴇsᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}dspam</code> [ᴊᴜᴍʟᴀʜ_ᴘᴇsᴀɴ - ᴊᴜᴍʟᴀʜ_ᴅᴇʟᴀʏ_ᴅᴇᴛɪᴋ - ᴘᴇsᴀɴ_sᴘᴀᴍ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ sᴘᴀᴍ ᴘᴇsᴀɴ ᴅᴇʟᴀʏ
"""


@PY.UBOT("spam")
async def _(client, message):
    await spam_cmd(client, message)


@PY.UBOT("dspam")
async def _(client, message):
    await dspam_cmd(client, message)
