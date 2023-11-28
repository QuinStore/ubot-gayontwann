import motor
import asyncio
from pyrogram import enums, filters, Client
from pyrogram.types import Message
from PyroUbot.config import MONGO_URL
from PyroUbot import *
from PyroUbot.core.helpers.botlogs import izzy_meira


cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
collection = cli["tag_log"]


async def get_log(user_id: int):
    result = await collection.users.find_one({'user_id': user_id})
    if not result:
        return None
    return result['tag_log']


async def idup_log(user_id: int, message: Message) -> bool:
    log = {"user_id": user_id}
    try:
        result = await collection.users.update_one(
            {'user_id': user_id},
            {'$set': {'tag_log': True}},
            upsert=True
        )
        if result.modified_count > 0 or result.upserted_id:
            await log_tagged_messages()
            return True
    except:
        return False


async def mati_log(user_id: int, message: Message) -> bool:
    log = {"user_id": user_id}
    try:
        result = await collection.users.update_one(
            {'user_id': user_id},
            {'$set': {'tag_log': False}},
            upsert=True
        )
        if result.modified_count > 0 or result.upserted_id:
            return False
    except:
        return False


@ubot.on_message(
    filters.group
    & filters.mentioned
    & filters.incoming
    & ~filters.bot
    & ~filters.via_bot,
    group=69,
)
async def log_tagged_messages(client, message: Message):
    logger = await get_log(client.me.id)
    if not logger:
        return
    user_id = message.from_user.id
    txt = f"Pesan Baru\n• : {message.from_user.mention}"
    if message.chat.type == "group" or message.chat.type == "supergroup":
        txt += f"\n• Group : {message.chat.title}"
    else:
        txt += f"\n• User : {message.from_user.first_name}"
    txt += f"\n• Link Pesan : <a href='{message.link}'>{message.chat.title}</a>"
    txt += f"\n• Pesan : {message.text}"
    await asyncio.sleep(0.1)
    group = await izzy_meira(client)
    await client.send_message(
        group.id,
        txt,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
        )
        #await client.send_message(
        #    "me",
        #    txt,
        #    parse_mode=enums.ParseMode.HTML,
        #    disable_web_page_preview=True,
        #)

@PY.UBOT("log")
async def set_log(client, message):
    user_id = message.from_user.id
    await idup_log(user_id, message)
    await message.edit("`Logger Tag Berhasil Dihidupkan`"
            )


@PY.UBOT("nolog")
async def set_no_log(client, message):
    user_id = message.from_user.id
    await mati_log(user_id, message)
    await message.edit("`Logger Tag Berhasil Dimatikan`"
            )