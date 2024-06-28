from PyroUbot import *

__MODULE__ = "dbcontrol"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴅʙᴄᴏɴᴛʀᴏʟ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cekuser</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴄᴇᴋ ᴅᴀᴛᴀʙᴀꜱᴇ ʙᴇʀᴀᴘᴀ ᴜꜱᴇʀ ʏᴀɴɢ ꜱᴜᴅᴀʜ ᴍᴇᴍᴀᴋᴀɪ 
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}prem</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴋᴇ ᴅᴀᴛᴀʙᴀꜱᴇ ᴘʀᴇᴍɪᴜᴍ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unprem</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴɢʜᴀᴘᴜꜱ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴋᴇ ᴅᴀᴛᴀʙᴀꜱᴇ ᴘʀᴇᴍɪᴜᴍ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}seles</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴋᴇ ᴅᴀᴛᴀʙᴀꜱᴇ ʀᴇꜱᴇʟʟᴇʀ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unseles</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴɢʜᴀᴘᴜꜱ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴋᴇ ᴅᴀᴛᴀʙᴀꜱᴇ ʀᴇꜱᴇʟʟᴇʀ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}getprem</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴄᴇᴋ ᴅᴀᴛᴀʙᴀꜱᴇ ʟɪꜱᴛ ᴜꜱᴇʀ ᴛᴇʀʜᴜʙᴜɴɢ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}getseles</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴄᴇᴋ ᴅᴀᴛᴀʙᴀꜱᴇ ʟɪꜱᴛ ᴜꜱᴇʀ ᴛᴇʀʜᴜʙᴜɴɢ 
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cek</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴄᴇᴋ ᴅᴀᴛᴀʙᴀꜱᴇ ᴇxᴘɪʀᴇᴅ ꜱᴇꜱᴇᴏʀᴀɴɢ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}time</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴᴀᴍʙᴀʜ ᴡᴀᴋᴛᴜ ᴇxᴘɪʀᴇᴅ ꜱᴇꜱᴇᴏʀᴀɴɢ  
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}untime</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇʀᴇꜱᴇᴛ ᴇxᴘɪʀᴇᴅ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴍᴇɴᴊᴀᴅɪ 30 ᴅᴀʏ
  
"""

@PY.BOT("prem")
@PY.UBOT("prem")
async def _(client, message):
    await prem_user(client, message)

@PY.BOT("cekuser", FILTERS.OWNER)
@PY.UBOT("cekuser", FILTERS.ME_OWNER)
async def _(client, message):
    await jumlah_user(client, message)
    
@PY.BOT("unprem", FILTERS.OWNER)
@PY.UBOT("unprem", FILTERS.ME_OWNER)
async def _(client, message):
    await unprem_user(client, message)


@PY.BOT("getprem", FILTERS.OWNER)
@PY.UBOT("getprem", FILTERS.ME_OWNER)
async def _(cliebt, message):
    await get_prem_user(client, message)


@PY.BOT("seles", FILTERS.OWNER)
@PY.UBOT("seles", FILTERS.ME_OWNER)
async def _(client, message):
    await seles_user(client, message)


@PY.BOT("unseles", FILTERS.OWNER)
@PY.UBOT("unseles", FILTERS.ME_OWNER)
async def _(client, message):
    await unseles_user(client, message)


@PY.BOT("getseles", FILTERS.OWNER)
@PY.UBOT("getseles", FILTERS.ME_OWNER)
async def _(client, message):
    await get_seles_user(client, message)


@PY.BOT("time", FILTERS.OWNER)
@PY.UBOT("time", FILTERS.ME_OWNER)
async def _(client, message):
    await expired_add(client, message)


@PY.BOT("cek", FILTERS.OWNER)
@PY.UBOT("cek", FILTERS.ME_OWNER)
async def _(client, message):
    await expired_cek(client, message)


@PY.BOT("untime", FILTERS.OWNER)
@PY.UBOT("untime", FILTERS.ME_OWNER)
async def _(client, message):
    await un_expired(client, message)


@PY.CALLBACK("restart")
async def _(client, callback_query):
    await cb_restart(client, callback_query)


@PY.CALLBACK("gitpull")
async def _(client, callback_query):
    await cb_gitpull(client, callback_query)
