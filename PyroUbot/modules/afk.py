from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from PyroUbot.core.database.afk import check_afk, go_afk, no_afk
from PyroUbot.core.helpers.botlogs import izzy_meira
from PyroUbot.core.database.variabel import get_vars, set_vars
from PyroUbot import PY, ubot

__MODULE__ = "Afk"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀғᴋ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}afk</code> alasan
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴍᴏᴅᴇ ᴀғᴋ

<b>ᴍɪsᴄ:</b>
  .setemoji afkon: ɢᴀɴᴛɪ ᴇᴍᴏᴊɪ ᴀғᴋ
  .setemoji afkwaktu: ɢᴀɴᴛɪ ᴇᴍᴏᴊɪ ᴡᴀᴋᴛᴜ ᴀғᴋ
  .setemoji afkalasan: ɢᴀɴᴛɪ ᴇᴍᴏᴊɪ ᴀʟᴀsᴀɴ ᴀғᴋ
  .setemoji afkonline: ɢᴀɴᴛɪ ᴇᴍᴏᴊɪ ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ
"""

afk_sanity_check: dict = {}
afkstr = """
#ᴀғᴋ\nᴀʟᴀsᴀɴ {}
"""
onlinestr = """
#ᴏɴʟɪɴᴇ\nᴀʟᴀsᴀɴ {}
"""

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

async def is_afk_(f, client, message):
    user_id = client.me.id
    af_k_c = await check_afk(user_id)
    return bool(af_k_c)


is_afk = filters.create(func=is_afk_, name="is_afk_")

@PY.UBOT("afk")
async def set_afk(client, message):
    emot_9 = await get_vars(client.me.id, "EMOJI_PROSES")
    emot_10 = await get_vars(client.me.id, "EMOJI_SUKSES")
    emot_11 = await get_vars(client.me.id, "EMOJI_ERROR")
    emot_afk = emot_9 if emot_9 else "5467890025217661107"
    emot_waktu_afk = emot_10 if emot_10 else "5451732530048802485"
    emot_alasan = emot_11 if emot_11 else "5334882760735598374"
    if len(message.command) == 1:
        return await message.reply(
            f"ғᴏʀᴍᴀᴛ sᴀʟᴀʜ...\nᴄᴏɴᴛᴏʜ : <code>afk berak</code>",
        )
    user_id = client.me.id
    user= message.from_user.id
    group = await izzy_meira(client)
    izzy = await message.reply( "ᴍᴏᴅᴇ ᴀғᴋ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
    msge = None
    msge = get_text(message)
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if msge:
        if client.me.is_premium:
            msg = f"<emoji id={emot_afk}> sᴇᴅᴀɴɢ ᴀғᴋ,\n<emoji id={emot_alasan}>ᴀʟᴀsᴀɴ: {msge}"
        else:
            msg = f"❗️ sᴇᴅᴀɴɢ ᴀғᴋ,\n📝ᴀʟᴀsᴀɴ:: {msge}"
        await client.send_message(group.id, afkstr.format(msge))
        await go_afk(user_id, afk_start, msge)
    else:
        msg = "sᴇᴅᴀɴɢ ᴀғᴋ"
        await client.send_message(group.id, afkstr.format(msge))
        await go_afk(user_id, afk_start)
    await izzy.edit(msg)

@ubot.on_message(
    is_afk
    & (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.bot
    & filters.incoming
)
async def afk_er(client, message):
    emot_9 = await get_vars(client.me.id, "EMOJI_AFK")
    emot_10 = await get_vars(client.me.id, "EMOJI_WAKTU")
    emot_11 = await get_vars(client.me.id, "EMOJI_ALASAN")
    emot_afk = emot_9 if emot_9 else "5467890025217661107"
    emot_waktu_afk = emot_10 if emot_10 else "5451732530048802485"
    emot_alasan = emot_11 if emot_11 else "5334882760735598374"
    user_id = client.me.id
    if not message:
        return
    if not message.from_user:
        return
    if message.from_user.id == user_id:
        return
    use_r = int(user_id)
    if use_r not in afk_sanity_check.keys():
        afk_sanity_check[use_r] = 1
    else:
        afk_sanity_check[use_r] += 1
    if afk_sanity_check[use_r] == 5:
        await message.reply_text("sᴇᴅᴀɴɢ ᴀғᴋ")
        afk_sanity_check[use_r] += 1
        return
    if afk_sanity_check[use_r] > 5:
        return
    lol = await check_afk(user_id)
    reason = lol["reason"]
    if reason == "":
        reason = None
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    user = message.from_user.id
    if client.me.is_premium:
        message_to_reply = (
            f"<emoji id={emot_afk}> sᴇᴅᴀɴɢ ᴀғᴋ,\n<emoji id={emot_waktu_afk}> sᴇʟᴀᴍᴀ: {total_afk_time}\n<emoji id={emot_alasan}>ᴀʟᴀsᴀɴ: {reason}"
                if reason
            else f"<emoji id={emot_afk}> sᴇᴅᴀɴɢ ᴀғᴋ,\n<emoji id={emot_waktu_afk}> sᴇʟᴀᴍᴀ: {total_afk_time}"
    )
    else:
        message_to_reply = (
        f"❗️ sᴇᴅᴀɴɢ ᴀғᴋ,\n⌛️sᴇʟᴀᴍᴀ: {total_afk_time}\n📝ᴀʟᴀsᴀɴ: {reason}"
        if reason
        else f"❗️ sᴇᴅᴀɴɢ ᴀғᴋ\n⌛️sᴇʟᴀᴍᴀ: {total_afk_time}"
    )
    await message.reply(message_to_reply)


@ubot.on_message(filters.outgoing & filters.me & is_afk)
async def no_afke(client, message):
    emot_10 = await get_vars(client.me.id, "EMOJI_WAKTU")
    emot_12 = await get_vars(client.me.id, "EMOJI_ONLINE")
    emoat_online= emot_12 if emot_12 else "5467596412663372909"
    emot_waktu_afk = emot_10 if emot_10 else "5451732530048802485"
    user_id = client.me.id
    group = await izzy_meira(client)
    lol = await check_afk(user_id)
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    user = message.from_user.id
    if client.me.is_premium:
        kk = await message.reply(f"✅ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ.\n⌛️ᴡᴀᴋᴛᴜ ᴀғᴋ: {total_afk_time}")   
    else:            
        kk = await message.reply(f"✅ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ.\n⌛️ᴡᴀᴋᴛᴜ ᴀғᴋ: {total_afk_time}")
    await kk.delete()
    await no_afk(user_id)
    await client.send_message(group.id, onlinestr.format(total_afk_time))
