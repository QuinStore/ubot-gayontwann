from PyroUbot import *

__MODULE__ = "notes"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴᴏᴛᴇs 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addnote</code> [ɴᴏᴛᴇ_ɴᴀᴍᴇ - ʀᴇᴘʟʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴʏɪᴍᴘᴀɴ sᴇʙᴜᴀʜ ᴄᴀᴛᴀᴛᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}get</code> [ɴᴏᴛᴇ_ɴᴀᴍᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴄᴀᴛᴀᴛᴀɴ ʏᴀɴɢ ᴅɪsɪᴍᴘᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delnote</code> [ɴᴏᴛᴇ_ɴᴀᴍᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴄᴀᴛᴀᴛᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}notes</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ ᴄᴀᴛᴀᴛᴀɴ ʏᴀɴɢ ᴅɪsɪᴍᴘᴀɴ

  <b>ɴᴏᴛᴇ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴜᴛᴛᴏɴ, ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ:</b>
  <code>ᴛᴇxᴛ ~> ʙᴜᴛᴛᴏɴ_ᴛᴇxᴛ:ʙᴜᴛᴛᴏɴ_ᴜʀʟ</code>
"""


@PY.UBOT("addnote")
async def add_note(client, message):
    await addnote_cmd(client, message)


@PY.UBOT("get")
async def get_note(client, message):
    await get_cmd(client, message)


@PY.INLINE("^get_notes")
@INLINE.QUERY
async def _(client, inline_query):
    await get_notes_button(client, inline_query)


@PY.UBOT("delnote")
async def _(client, message):
    await delnote_cmd(client, message)


@PY.UBOT("notes")
async def _(client, message):
    await notes_cmd(client, message)
