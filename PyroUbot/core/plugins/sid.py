from PyroUbot import *


async def id_cmd(client, message):
    text = f"<b><a href={message.link}>ᴍᴇssᴀɢᴇ ɪᴅ:</a></b> <code>{message.id}</code>\n"

    if message.chat.type == ChatType.CHANNEL:
        text += f"<b><a href=https://t.me/{message.chat.username}>ᴄʜᴀᴛ ɪᴅ:</a></b> <code>{message.sender_chat.id}</code>\n"
    else:
        text += f"<b><a href=tg://user?id={message.from_user.id}>ʏᴏᴜʀ ɪᴅ:</a></b> <code>{message.from_user.id}</code>\n\n"

        if len(message.command) > 1:
            try:
                user = await client.get_chat(message.text.split()[1])
                text += f"<b><a href=tg://user?id={user.id}>ᴜsᴇʀ ɪᴅ:</a></b> <code>{user.id}</code>\n\n"
            except:
                return await message.reply("Pengguna tidak ditemukan.")

        text += f"<b><a href=https://t.me/{message.chat.username}>ᴄʜᴀᴛ ɪᴅ:</a></b> <code>{message.chat.id}</code>\n\n"

    if message.reply_to_message:
        id_ = (
            message.reply_to_message.from_user.id
            if message.reply_to_message.from_user
            else message.reply_to_message.sender_chat.id
        )
        file_info = get_file_id(message.reply_to_message)
        if file_info:
            text += f"<b><a href={message.reply_to_message.link}>ᴍᴇᴅɪᴀ ɪᴅ:</a> <code>{file_info.file_id}</code>\n\n"
        text += (
            f"<b><a href={message.reply_to_message.link}>ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:</a></b> <code>{message.reply_to_message.id}</code>\n"
            f"<b><a href=tg://user?id={id_}>ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:</a></b> <code>{id_}</code>"
        )

    return await message.reply(text, disable_web_page_preview=True)
