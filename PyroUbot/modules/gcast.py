from PyroUbot import *

__MODULE__ = "gcast"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ucast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴜsᴇʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}gcast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}fgcast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ʟᴇᴡᴀᴛɪ ᴀɴᴛɪ ɢᴄᴀsᴛ ʙᴏᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}spamg</code>[ᴊᴜᴍʟᴀʜ] [ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ sᴘᴀᴍ ɢɪᴋᴇs ᴘᴇsᴀɴ ᴋᴇ ɢʀᴏᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}bgcast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ʟᴇᴡᴀᴛɪ ᴀɴᴛɪ ɢᴄᴀsᴛ ʙᴏᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}send</code> [ᴜsᴇʀɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ᴛᴇxᴛ/ʀᴇᴘʟʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ ᴜsᴇʀ/ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ
  

  <b>ᴍɪsᴄ:</b>
  .setemoji proses: ɢᴀɴᴛɪ ᴇᴍᴏᴊɪ ᴘʀᴏsᴇs gcast
  .setemoji sukses: ɢᴀɴᴛɪ ᴇᴍᴏᴊɪ sᴜᴋsᴇs gcast
  .setemoji error: ɢᴀɴᴛɪ ᴇᴍᴏᴊɪ ɢᴀɢᴀʟ ɢᴄᴀsᴛ

  .setproses: ɢᴀɴᴛɪ ᴋᴀᴛᴀ-ᴋᴀᴛᴀ ᴘʀᴏsᴇs ɢᴄᴀsᴛ
  .setsukses: ɢᴀɴᴛɪ ᴋᴀᴛᴀ-ᴋᴀᴛᴀ sᴇʟᴇsᴀɪ ɢᴄᴀsᴛ
  
"""

@PY.UBOT("setproses")
async def _(client, message):
    await set_proses_message(client, message)

@PY.UBOT("setsukses")
async def _(client, message):
    await set_sukses_message(client, message)

@PY.UBOT("setpong")
async def _(client, message):
    await set_pong_message(client, message)

@PY.UBOT("spamg")
async def _(client, message):
    await broadcast_group_spam(client, message)

@PY.UBOT("setuptime")
async def _(client, message):
    await set_uptime_message(client, message)

@PY.UBOT("setmention")
async def _(client, message):
    await set_mention_message(client, message)

@ubot.on_message(filters.command("gcast", "$") & filters.user(SUDO_USERS))
@PY.UBOT("gcast")
async def _(client, message):
    await broadcast_group_cmd(client, message)

@ubot.on_message(filters.command("bgcast", "$") & filters.user(SUDO_USERS))
@PY.UBOT("bgcast")
async def _(client, message):
    await blue_gcast(client, message)

@ubot.on_message(filters.command("fgcast", "$") & filters.user(SUDO_USERS))
@PY.UBOT("fgcast")
async def _(client, message):
    await broadcast_cmd(client, message)


@PY.UBOT("ucast")
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.BOT("send")
@PY.UBOT("send")
async def _(client, message):
    await send_msg_cmd(client, message)


@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)
