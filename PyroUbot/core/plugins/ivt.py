import asyncio

from pyrogram.enums import UserStatus

from PyroUbot import *


async def invite_cmd(client, message):
    mg = await message.reply("<b>ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ!</b>")
    if len(message.command) < 2:
        return await mg.delete()
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit(
            "<b>ʙᴇʀɪ sᴀʏᴀ ᴘᴇɴɢɢᴜɴᴀ ᴜɴᴛᴜᴋ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ! ᴘᴇʀɪᴋsᴀ ᴍᴇɴᴜ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴꜰᴏ ʟᴇʙɪʜ ʟᴀɴᴊᴜᴛ!</b>"
        )
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except Exception as e:
        return await mg.edit(f"{e}")
    await mg.edit(f"<b>ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ {len(user_list)} ᴋᴇ ɢʀᴜᴘ ɪɴɪ</b>")


invite_id = []


async def inviteall_cmd(client, message):
    Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if len(message.command) < 3:
        await message.delete()
        return await Tm.delete()
    try:
        chat = await client.get_chat(message.command[1])
    except Exception as error:
        return await Tm.edit(error)
    if message.chat.id in invite_id:
        return await Tm.edit_text(
            f"sᴇᴅᴀɴɢ ᴍᴇɴɢɪɴᴠɪᴛᴇ ᴍᴇᴍʙᴇʀ sɪʟᴀʜᴋᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴀᴛᴀᴜ ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ: <code>{PREFIX[0]}cancel</code>"
        )
    else:
        done = 0
        failed = 0
        invite_id.append(message.chat.id)
        await Tm.edit_text(f"ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ {chat.title}")
        async for member in client.get_chat_members(chat.id):
            stats = [
                UserStatus.ONLINE,
                UserStatus.OFFLINE,
                UserStatus.RECENTLY,
                UserStatus.LAST_WEEK,
            ]
            if member.user.status in stats:
                try:
                    await client.add_chat_members(message.chat.id, member.user.id)
                    done = done + 1
                    await asyncio.sleep(int(message.command[2]))
                except Exception:
                    failed = failed + 1
                    await asyncio.sleep(int(message.command[2]))
        invite_id.remove(message.chat.id)
        await Tm.delete()
        return await message.reply(
            f"""
<b>✅ <code>{done}</code> ᴀɴɢɢᴏᴛᴀ ʏᴀɴɢ ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴᴅᴀɴɢ</b>
<b>❌ <code>{failed}</code> ᴀɴɢɢᴏᴛᴀ ʏᴀɴɢ ɢᴀɢᴀʟ ᴅɪᴜɴᴅᴀɴɢ</b>
"""
        )


async def cancel_cmd(client, message):
    if message.chat.id not in invite_id:
        return await message.reply_text(
            f"sᴇᴅᴀɴɢ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇʀɪɴᴛᴀʜ: <code>{PREFIX[0]}inviteall</code> ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ"
        )
    try:
        invite_id.remove(message.chat.id)
        await message.reply_text("ok inviteall berhasil dibatalkan")
    except Exception as e:
        await message.reply_text(e)
