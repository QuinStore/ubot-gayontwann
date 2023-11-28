from PyroUbot import *

__MODULE__ = "qrcode"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ǫʀᴄᴏᴅᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}qrGen</code> [ᴛᴇxᴛ ǫʀᴄᴏᴅᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ǫʀᴄᴏᴅᴇ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}qrRead</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ǫʀᴄᴏᴅᴇ ᴍᴇɴᴊᴀᴅɪ ᴛᴇxᴛ
"""


@PY.UBOT("qrgen")
async def _(client, message):
    await qr_gen_cmd(client, message)


@PY.UBOT("qrread")
async def _(client, message):
    await qr_read_cmd(client, message)
