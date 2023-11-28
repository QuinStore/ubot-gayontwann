import asyncio
import os
from gc import get_objects
from time import time

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InputTextMessageContent)

from PyroUbot import *


async def copy_bot_msg(client, message):
    if message.from_user.id not in ubot._get_my_id:
        return
    Tm = await message.reply("ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )
    msg_id = int(link.split("/")[-1])
    chat = str(link.split("/")[-2])
    try:
        get = await client.get_messages(chat, msg_id)
        await get.copy(message.chat.id)
        await Tm.delete()
    except Exception as error:
        await Tm.edit(error)


COPY_ID = {}


async def download_media_copy(get, client, infomsg, message):
    msg = message.reply_to_message or message
    text = get.caption or ""
    if get.photo:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴘʜᴏᴛᴏ",
                get.photo.file_id,
            ),
        )
        await client.send_photo(
            message.chat.id,
            media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)

    elif get.animation:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴɪᴍᴀᴛɪᴏɴ",
                get.animation.file_id,
            ),
        )
        await client.send_animation(
            message.chat.id,
            animation=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)

    elif get.voice:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(infomsg, time(), "ᴅᴏᴡɴʟᴏᴀᴅ ᴠᴏɪᴄᴇ", get.voice.file_id),
        )
        await client.send_voice(
            message.chat.id,
            voice=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)

    elif get.audio:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴀᴜᴅɪᴏ",
                get.audio.file_id,
            ),
        )
        thumbnail = await client.download_media(get.audio.thumbs[-1]) or None
        await client.send_audio(
            message.chat.id,
            audio=media,
            duration=get.audio.duration,
            caption=text,
            thumb=thumbnail,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)
        os.remove(thumbnail)

    elif get.document:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴅᴏᴄᴜᴍᴇɴᴛ",
                get.document.file_id,
            ),
        )
        await client.send_document(
            message.chat.id,
            document=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)

    elif get.video:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ",
                get.video.file_name,
            ),
        )
        thumbnail = await client.download_media(get.video.thumbs[-1]) or None
        await client.send_video(
            message.chat.id,
            video=media,
            duration=get.video.duration,
            caption=text,
            thumb=thumbnail,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)
        os.remove(thumbnail)


async def copy_ubot_msg(client, message):
    msg = message.reply_to_message or message
    infomsg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴄᴏᴘʏ ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ</b>")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
            try:
                get = await client.get_messages(chat, msg_id)
                try:
                    await get.copy(message.chat.id, reply_to_message_id=msg.id)
                    await infomsg.delete()
                except Exception:
                    await download_media_copy(get, client, infomsg, message)
            except Exception as e:
                await infomsg.edit(str(e))
        else:
            chat = str(link.split("/")[-2])
            try:
                get = await client.get_messages(chat, msg_id)
                await get.copy(message.chat.id, reply_to_message_id=msg.id)
                await infomsg.delete()
            except Exception:
                try:
                    text = f"get_msg {id(message)}"
                    x = await client.get_inline_bot_results(bot.me.username, text)
                    results = await client.send_inline_bot_result(
                        message.chat.id,
                        x.query_id,
                        x.results[0].id,
                        reply_to_message_id=msg.id,
                    )
                    COPY_ID[client.me.id] = int(results.updates[0].id)
                    await infomsg.delete()
                except Exception as error:
                    await infomsg.edit(f"{str(error)}")
    else:
        await infomsg.edit("ᴍᴀsᴜᴋᴋɪɴ ʟɪɴᴋ ʏᴀɴɢ ᴠᴀʟɪᴅ")


async def copy_inline_msg(client, inline_query):
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get message!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="🔐 ʙᴜᴋᴀ ᴋᴏɴᴛᴇɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ 🔐",
                                    callback_data=f"copymsg_{int(inline_query.query.split()[1])}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTextMessageContent(
                        "<b>🔒 ᴋᴏɴᴛᴇɴ ʏᴀɴɢ ᴍᴀᴜ ᴅɪᴀᴍʙɪʟ ʙᴇʀsɪꜰᴀᴛ ʀᴇsᴛʀɪᴄᴛᴇᴅ\n\n✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ᴋᴏɴᴛᴇɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ</b>"
                    ),
                )
            )
        ],
    )


async def copy_callback_msg(client, callback_query):
    try:
        q = int(callback_query.data.split("_", 1)[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        await m._client.unblock_user(bot.me.username)
        await callback_query.edit_message_text("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
        copy = await m._client.send_message(
            bot.me.username, f"/copy {m.text.split()[1]}"
        )
        msg = m.reply_to_message or m
        await asyncio.sleep(1.5)
        await copy.delete()
        async for get in m._client.search_messages(bot.me.username, limit=1):
            await m._client.copy_message(
                m.chat.id, bot.me.username, get.id, reply_to_message_id=msg.id
            )
            await m._client.delete_messages(m.chat.id, COPY_ID[m._client.me.id])
            await get.delete()
    except Exception as error:
        await callback_query.edit_message_text(f"<code>{error}</code>")
