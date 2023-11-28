from asyncio import gather
from os import remove

from pyrogram.enums import ChatType

from PyroUbot import *


async def info_cmd(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("</b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<bʙᴇʀɪᴋᴀɴ ᴜsᴇʀɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏ ᴘᴇɴɢɢᴜɴᴀ ᴛᴇʀsᴇʙᴜᴛ.></b>"
        )
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""
<b>ᴜsᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ:</b>

🆔 <b>ᴜsᴇʀ ɪᴅ:</b> <code>{user.id}</code>
👤 <b>ꜰɪʀsᴛ ɴᴀᴍᴇ:</b> {first_name}
🗣️ <b>ʟᴀsᴛ ɴᴀᴍᴇ:</b> {last_name}
🌐 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> {username}
🏛️ <b>ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>
🤖 <b>ɪs ʙᴏᴛ:</b> <code>{user.is_bot}</code>
🚷 <b>ɪs sᴄᴀᴍ:</b> <code>{user.is_scam}</code>
🚫 <b>ʀᴇsᴛʀɪᴄᴛᴇᴅ:</b> <code>{user.is_restricted}</code>
✅ <b>ᴠᴇʀɪꜰɪᴇᴅ:</b> <code>{user.is_verified}</code>
⭐ <b>ᴘʀᴇᴍɪᴜᴍ:</b> <code>{user.is_premium}</code>
📝 <b>ᴜsᴇʀ ʙɪᴏ:</b> {bio}

👀 <b>sᴀᴍᴇ ɢʀᴏᴜᴘs sᴇᴇɴ:</b> {len(common)}
👁️ <b>ʟᴀsᴛ sᴇᴇɴ:</b> <code>{status}</code>
🔗 <b>ᴜsᴇʀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ:</b> <a href=tg://user?id={user.id}>{fullname}</a>
"""
        photo_id = user.photo.big_file_id if user.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"ɪɴꜰᴏ: {e}")


async def cinfo_cmd(client, message):
    Tm = await message.reply("</b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    try:
        if len(message.text.split()) > 1:
            chat_u = message.text.split()[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await Tm.edit(
                    f"ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ ᴀᴛᴀᴜ ɢᴜɴᴀᴋᴀɴ {PREFIX[0]}cinfo [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴀᴛᴀᴜ ɪᴅ]"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""
<b>ᴄʜᴀᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ:</b>

🆔 <b>ᴄʜᴀᴛ ɪᴅ:</b> <code>{chat.id}</code>
👥 <b>ᴛɪᴛʟᴇ:</b> {chat.title}
👥 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> {username}
📩 <b>ᴛʏᴘᴇ:</b> <code>{type}</code>
🏛️ <b>ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>
🗣️ <b>ɪs sᴄᴀᴍ:</b> <code>{chat.is_scam}</code>
🎭 <b>ɪs ꜰᴀᴋᴇ:</b> <code>{chat.is_fake}</code>
✅ <b>ᴠᴇʀɪꜰɪᴇᴅ:</b> <code>{chat.is_verified}</code>
🚫 <b>ʀᴇsᴛʀɪᴄᴛᴇᴅ:</b> <code>{chat.is_restricted}</code>
🔰 <b>ᴘʀᴏᴛᴇᴄᴛᴇᴅ:</b> <code>{chat.has_protected_content}</code>

🚻 <b>ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs:</b> <code>{chat.members_count}</code>
📝 <b>ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:</b> <code>{description}</code>
"""
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"ɪɴꜰᴏ: `{e}`")
