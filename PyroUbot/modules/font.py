from PyroUbot import *

__MODULE__ = "font"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜰᴏɴᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}font</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇxᴛ ꜰᴏɴᴛ ᴅᴇɴɢᴀɴ ᴛᴀᴍᴘɪʟᴀɴ ʏᴀɴɢ ʙᴇʀʙᴇᴅᴀ
"""


@PY.UBOT("font")
async def _(client, message):
    await font_message(client, message)


@PY.INLINE("^get_font")
@INLINE.QUERY
async def _(client, inline_query):
    await font_inline(client, inline_query)


@PY.CALLBACK("^get")
@INLINE.DATA
async def _(client, callback_query):
    await font_callback(client, callback_query)


@PY.CALLBACK("^next")
@INLINE.DATA
async def _(client, callback_query):
    await font_next(client, callback_query)


@PY.CALLBACK("^prev")
@INLINE.DATA
async def _(client, callback_query):
    await font_prev(client, callback_query)
