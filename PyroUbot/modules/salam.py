
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot.core.helpers.msg_type import ReplyCheck
from PyroUbot import *


@ubot.on_message(filters.command("p") & filters.me)
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum...",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("pe") & filters.me)
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("l") & filters.me)
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam...",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("wl") & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("as") & filters.me)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu..")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")


__MODULE__ = "ꜱᴀʟᴀᴍ"
__HELP__ = f"""
Bantuan Untuk Salam

๏ Perintah: <code>.p</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>.pe</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>.l</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>.wl</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>.as</code>
◉ Penjelasan: Coba sendiri.
"""
