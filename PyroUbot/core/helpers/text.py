from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import LOGS_MAKER_UBOT, OWNER_ID, bot, get_expired_date, ubot


class MSG:
    def DEAK(X):
        return (
            f"""
<b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs ᴅᴀʀɪ ᴛᴇʟᴇɢʀᴀᴍ</b>
""",
        )

    def EXPIRED_MSG_BOT(X):
        return f"""
<b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b>
"""

    def START(message):
        if not message.from_user.id == OWNER_ID:
            msg = f"""
<b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

💬 @{bot.me.username} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ

🚀 ꜱɪʟᴀʜᴋᴀɴ ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ 
• ᴏᴡɴᴇʀ : <a href=tg://openmessage?user_id={OWNER_ID}>𝐐𝐮𝐞𝐞𝐧</a> 

👉🏻 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>
"""
        else:
            msg = f"""
🧑‍💻 ᴍᴏᴅᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>

🚀 ꜱɪʟᴀʜᴋᴀɴ ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ 
• ᴏᴡɴᴇʀ : <a href=tg://openmessage?user_id={OWNER_ID}>𝐐𝐮𝐞𝐞𝐧</a> 

✅ ɢᴜɴᴀᴋᴀɴʟᴀʜ ᴛᴏᴍʙᴏɪ ᴅɪ ʙᴀᴡᴀʜ ᴅᴇɴɢᴀɴ ʙɪᴊᴀᴋ
"""
        return msg

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├ ᴅᴀɴᴀ/ᴏᴠᴏ</b>
 <b>├────• <code>085184965402</code></b>
<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ {total}.000</b>
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b> 

 🚀 ꜱɪʟᴀʜᴋᴀɴ ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ 
• ᴏᴡɴᴇʀ : <a href=tg://openmessage?user_id={OWNER_ID}>𝐐𝐮𝐞𝐞𝐧</a> 

<b>✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b>
"""

    def POLICY():
        return """
Dᴇɴɢᴀɴ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʟᴀʏᴀɴᴀɴ ᴋᴀᴍɪ, 
Aɴᴅᴀ ᴍᴇᴍᴇʀᴄᴀʏᴀᴋᴀɴ ɪɴғᴏʀᴍᴀsɪ Aɴᴅᴀ ᴋᴇᴘᴀᴅᴀ ᴋᴀᴍɪ. 
Kᴀᴍɪ ᴘᴀʜᴀᴍ ʙᴀʜᴡᴀ ᴍᴇʟɪɴᴅᴜɴɢɪ ɪɴғᴏʀᴍᴀsɪ Aɴᴅᴀ 
ᴅᴀɴ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴋᴏɴᴛʀᴏʟ ᴋᴇᴘᴀᴅᴀ Aɴᴅᴀ ᴀᴅᴀʟᴀʜ ᴛᴀɴɢɢᴜɴɢ ᴊᴀᴡᴀʙ ʏᴀɴɢ ʙᴇsᴀʀ 
ᴅᴀɴ ᴍᴇᴍᴇʀʟᴜᴋᴀɴ ᴋᴇʀᴊᴀ ᴋᴇʀᴀs.

ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʟᴀɴᴊᴜᴛᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴʏᴀᴛᴀᴋᴀɴ ʙᴀʜᴡᴀ ᴀɴᴅᴀ ᴛᴇʟᴀʜ 
ᴍᴇᴍʙᴀᴄᴀ ᴅᴀɴ ᴍᴇɴᴇʀɪᴍᴀ ᴋᴇᴛᴇɴᴛᴜᴀɴ ɪɴɪ ᴅᴀɴ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ 
ᴘᴇᴍʙᴇʟɪᴀɴ.
"""

    async def USERBOT(count):
        expired_date = await get_expired_date(ubot._ubot[int(count)].me.id)
        return f"""
<b>❏ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ├ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b> ╰ ᴇxᴘɪʀᴇᴅ</b> <code>{expired_date.strftime('%d-%m-%Y')}</code>
"""


async def sending_user(user_id):
    try:
        await bot.send_message(
            user_id,
            "💬 sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ᴀɴᴅᴀ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔥 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🔥",
                            callback_data="bahan",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )
        await bot.send_message(
            LOGS_MAKER_UBOT,
            f"""
➡️ ʏᴀɴɢ ᴍᴇʀᴀsᴀ ᴍᴇᴍɪʟɪᴋɪ ɪᴅ: {user_id}

✅ sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ɴʏᴀ ᴅɪ: @{bot.me.username}
    """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                            callback_data=f"cek_masa_aktif {user_id}",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        await bot.send_message(
            LOGS_MAKER_UBOT,
            f"""
➡️ ʏᴀɴɢ ᴍᴇʀᴀsᴀ ᴍᴇᴍɪʟɪᴋɪ ɪᴅ: {user_id}

✅ sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ɴʏᴀ ᴅɪ: @{bot.me.username}
    """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                            callback_data=f"cek_masa_aktif {user_id}",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )
        
