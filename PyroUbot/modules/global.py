from PyroUbot import *
DEV = [1998135373, 6619405249, 874946835]
__MODULE__ = "global"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʟᴏʙᴀʟ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}gban</ᴄᴏᴅᴇ> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ungban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ
"""

@ubot.on_message(filters.command("cgban", ".") & filters.user(DEV))
@PY.UBOT("gban")
async def global_banned(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("</b>ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not user_id:
        return await Tm.edit("<b>ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "<b>💬 ɢʟᴏʙᴀʟ {}</b>\n\n<b>✅ ʙᴇʀʜᴀsɪʟ: {} ᴄʜᴀᴛ</b>\n<b>❌ ɢᴀɢᴀʟ: {} ᴄʜᴀᴛ</b>\n<b>👤 ᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a></b>"
    global_id = await get_global_id(client, "global")
    for dialog in global_id:
        if user.id == OWNER_ID:
            return await Tm.edit("ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ɢʙᴀɴ ᴅɪᴀ ᴋᴀʀᴇɴᴀ ᴅɪᴀ ᴘᴇᴍʙᴜᴀᴛ sᴀʏᴀ")
        try:
            await client.ban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "ʙᴀɴɴᴇᴅ", done, failed, user.id, user.first_name, (user.last_name or "")
        )
    )
    return await Tm.delete()

@PY.UBOT("cungban", FILTERS.ME_OWNER)
@PY.UBOT("ungban")
async def global_unbanned(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("</b>ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not user_id:
        return await Tm.edit("<b>ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "<b>💬 ɢʟᴏʙᴀʟ {}</b>\n\n<b>✅ ʙᴇʀʜᴀsɪʟ: {} ᴄʜᴀᴛ</b>\n<b>❌ ɢᴀɢᴀʟ: {} ᴄʜᴀᴛ</b>\n<b>👤 ᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a></b>"
    global_id = await get_global_id(client, "global")
    for dialog in global_id:
        try:
            await client.unban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "ᴜɴʙᴀɴɴᴇᴅ",
            done,
            failed,
            user.id,
            user.first_name,
            (user.last_name or ""),
        )
    )
    return await Tm.delete()
