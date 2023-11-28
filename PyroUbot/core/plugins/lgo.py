import asyncio

from pyrogram.raw.functions.messages import DeleteHistory

from PyroUbot import *


async def logo_cmd(client, message):
    Tm = await message.reply("<code>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ...</code>")
    await client.unblock_user("@Yone_Robot")
    if message.reply_to_message:
        reply = message.reply_to_message
        if reply.photo or reply.animation or reply.sticker:
            rep_pic = await dl_pic(client, reply)
            send_pic = await client.send_photo("@Yone_Robot", rep_pic)
            text_pic = await send_pic.reply(
                f"/{message.command[0]} {message.text.split(None, 1)[1]}"
            )
            for X in (send_pic, text_pic):
                await X.delete()
        else:
            return await Tm.edit("ʀᴇᴘʟʏ ᴋᴇ ꜰᴏᴛᴏ/ɢɪꜰ/sᴛɪᴄᴋᴇʀ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʟᴏɢᴏ")
    else:
        if len(message.command) < 2:
            return await Tm.edit(
                f"<code>{message.text} [ᴛᴇxᴛ]</code> - ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʟᴏɢᴏ"
            )
        else:
            Tm_S = await client.send_message(
                "@Yone_Robot", f"/{message.command[0]} {message.text.split(None, 1)[1]}"
            )
            await Tm_S.delete()
    await Tm.edit("<code>sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs...</code>")
    await asyncio.sleep(8)
    async for msg in client.get_chat_history("@Yone_Robot"):
        try:
            if msg.photo:
                await message.reply_photo(
                    msg.photo.file_id,
                    caption=f"<b>ʟᴏɢᴏ ʙʏ:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>",
                )
                await Tm.delete()
            elif "Error Report" in msg.text:
                await Tm.edit(
                    "<b>ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ʟᴏɢᴏ sɪʟᴀʜᴋᴀɴ ᴜʟᴀɴɢɪ ʙᴇʙᴇʀᴀᴘᴀ sᴀᴀᴛ ʟᴀɢɪ</b>"
                )
        except:
            await Tm.edit("<code>ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ</code>")
        user_info = await client.resolve_peer("@Yone_Robot")
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
