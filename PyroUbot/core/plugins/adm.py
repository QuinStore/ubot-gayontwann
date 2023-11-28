from PyroUbot import *

__MODULE__ = "admin"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴍɪɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}kick</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙʟᴏᴋɪʀ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}mute</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unmute</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙʟᴏᴋɪʀᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙɪsᴜᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ
"""


@PY.UBOT("kick|dkick", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_kick(client, message)


@PY.UBOT("ban|dban", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_ban(client, message)


@PY.UBOT("mute|dmute", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_mute(client, message)


@PY.UBOT("unmute", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_unmute(client, message)


@PY.UBOT("unban", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_unban(client, message)
