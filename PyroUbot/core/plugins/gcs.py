import asyncio
from gc import get_objects

from pyrogram.enums import ChatType
from pyrogram.errors.exceptions import FloodWait

from PyroUbot import *
from PyroUbot.core.function.emoji import emoji

BLACKLIST_CHAT = [
 -1002125842026
]

def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg

async def get_broadcast_id(client, query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types[query]:
            chats.append(dialog.chat.id)

    return chats

async def broadcast_group_cmd(client, message):
    msg = await message.reply(emoji("proses") + f"sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ...")

    send = get_message(message)
    if not send:
        return await msg.edit(emoji("gagal") + f"ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ!.")

    chats = await get_broadcast_id(client, "group")
    blacklist = await get_chat(client.me.id)

    done = 0
    for chat_id in chats:
        if chat_id in blacklist:
            continue
        elif chat_id in BLACKLIST_CHAT:
            continue

        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"📊 ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ `{done}` ɢʀᴏᴜᴘ" + emoji("done"))    
    

async def broadcast_users_cmd(client, message):
    msg = await message.reply(emoji("proses") + f"sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ...")

    send = get_message(message)
    if not send:
        return await msg.edit(emoji("gagal") + f"ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ!.")

    chats = await get_broadcast_id(client, "users")

    done = 0
    for chat_id in chats:
        if chat_id == client.me.id:
            continue
        

        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"📊 ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ `{done}` ɢʀᴏᴜᴘ" + emoji("done"))    
    
async def set_proses_message(client: Client, message: Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)
    if len(args) >= 2:
        new_message = args[1]
        await set_gcast_process(user_id, new_message)
        await message.reply_text("ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ᴘᴇsᴀɴ ᴘʀᴏsᴇs..")
    else:
        await message.reply_text("ғᴏʀᴍᴀᴛ sᴀʟᴀʜ, ɢᴜɴᴀᴋᴀɴ '.setproses <kata kata>'.")

async def set_sukses_message(client: Client, message: Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)
    if len(args) >= 2:
        new_message = args[1]
        await set_gcast_sukses(user_id, new_message)
        await message.reply_text("ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ᴘᴇsᴀɴ sᴜᴋsᴇs")
    else:
        await message.reply_text("ғᴏʀᴍᴀᴛ sᴀʟᴀʜ, ɢᴜɴᴀᴋᴀɴ '.setsukses<kata kata>'")

async def send_msg_cmd(client, message):
    if message.reply_to_message:
        chat_id = (
            message.chat.id if len(message.command) < 2 else message.text.split()[1]
        )
        try:
            if client.me.id != bot.me.id:
                if message.reply_to_message.reply_markup:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    return await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await message.reply(error)
        else:
            try:
                return await message.reply_to_message.copy(chat_id)
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("ᴋᴇᴛɪᴋ ʏᴀɴɢ ʙᴇɴᴇʀ")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            return await client.send_message(chat_id, chat_text)
        except Exception as t:
            return await message.reply(f"{t}")


async def send_inline(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = next((obj for obj in get_objects() if id(obj) == _id), None)
    if m:
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ],
        )

def gcast_jahat(text):
    emoji_list = ["ぁ", "あ", "ぃ", "い", "ぅ", "う", "ぇ","え","ぉ","お","か","が","き","ぎ","く","ぐ","げ","こ","ご","け","み","さ","し","じ","す","ず","せ","ぜ","そ","ぞ","た","だ","ち","ぢ","っ","つ","づ","て","で","と","ど","な","に","ぬ","ね"] 
    words = text.split()
    replaced_text = " ".join([random.choice(emoji_list) + word for word in words])
    return replaced_text

async def broadcast_cmd(client, message):
    emot_4 = await get_vars(client.me.id, "EMOJI_PROSES")
    emot_5 = await get_vars(client.me.id, "EMOJI_SUKSES")
    emot_6 = await get_vars(client.me.id, "EMOJI_ERROR")
    emot_proses = emot_4 if emot_4 else "5972146261241892218"
    emot_sukses = emot_5 if emot_5 else "5852871561983299073"
    emot_error = emot_6 if emot_6 else "5852812849780362931"
    user_id = message.from_user.id
    gcast_msg = await load_gcast_messages(user_id)
    if client.me.is_premium:
        _proses = f"<emoji id={emot_proses}>😘</emoji> {gcast_msg['proses']}"
    else:
        _proses = gcast_msg["proses"]
    
    await message.reply(_proses)

    send = get_message(message)
    if not send:
        return await message.edit("ᴍᴏʜᴏн ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")

    chats = await get_global_id(client, "group")
    blacklist = await get_chat(client.me.id)
    
    meira = gcast_jahat(send)
    done = 0
    error = 0
    for chat_id in chats:
        if chat_id in blacklist:
            continue
        if chat_id not in blgc:

            try:
                await asyncio.sleep(1.5)
                if message.reply_to_message:
                    await meira.copy(chat_id)
                else:
                    await client.send_message(chat_id, meira)
                done += 1
                
            except FloodWait as e:
                await asyncio.sleep(e.value)
                if message.reply_to_message:
                    await send.meira(chat_id)
                else:
                    await client.send_message(chat_id, meira)
                done += 1
            except Exception:
                error += 1

    await message.delete()
    if client.me.is_premium:
        _sukses = f"{gcast_msg['sukses']}\n<b><emoji id={emot_sukses}>✅</emoji></b> {done} group,\n<emoji id={emot_error}>❌</emoji> {error} group"
    else:
        _sukses = f"{gcast_msg['sukses']}\n✅ {done} group\n❌ {error} group"

    return await message.reply(_sukses)


async def blue_gcast(client, message):
    emot_4 = await get_vars(client.me.id, "EMOJI_PROSES")
    emot_5 = await get_vars(client.me.id, "EMOJI_SUKSES")
    emot_6 = await get_vars(client.me.id, "EMOJI_ERROR")
    emot_proses = emot_4 if emot_4 else "5972146261241892218"
    emot_sukses = emot_5 if emot_5 else "5852871561983299073"
    emot_error = emot_6 if emot_6 else "5852812849780362931"
    user_id = message.from_user.id
    gcast_msg = await load_gcast_messages(user_id)
    
    if client.me.is_premium:
        _proses = f"<emoji id={emot_proses}>🔸</emoji> {gcast_msg['proses']}"
    else:
        _proses = gcast_msg["proses"]
    
    await message.reply(_proses)

    send = get_message(message)
    if not send:
        return await message.edit("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")

    chats = await get_global_id(client, "group")
    blacklist = await get_chat(client.me.id)
    error = 0
    done = 0
    
    for chat_id in chats:
        if chat_id in blacklist:
            continue
        if chat_id not in blgc:
            try:
                await asyncio.sleep(1.5)
                if message.reply_to_message:
                    await send.copy(chat_id)
                else:
                # Add backticks at the beginning and end of the message
                    await client.send_message(chat_id, f"`{send}`")
                done += 1
            except FloodWait as e:
                return await message.reply(f"ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛᴇʀᴋᴇɴᴀ ғʟᴏᴏᴅᴡᴀɪᴛ, sɪʟᴀʜᴋᴀɴ ᴛᴜɴɢɢᴜ {e.value}")
            except Exception:
                error += 1

    await message.delete()

    if client.me.is_premium:
        _sukses = f"{gcast_msg['sukses']}\n<b><emoji id={emot_sukses}>✅</emoji></b> {done} group,\n<emoji id={emot_error}>❌</emoji> {error} group"
    else:
        _sukses = f"{gcast_msg['sukses']}\n✅ {done} group\n❌ {error} group"

    return await message.reply(_sukses)        


async def broadcast_group_spam(client, message):
    emot_4 = await get_vars(client.me.id, "EMOJI_PROSES")
    emot_5 = await get_vars(client.me.id, "EMOJI_SUKSES")
    emot_6 = await get_vars(client.me.id, "EMOJI_ERROR")
    emot_proses = emot_4 if emot_4 else "5972146261241892218"
    emot_sukses = emot_5 if emot_5 else "5852871561983299073"
    emot_error = emot_6 if emot_6 else "5852812849780362931"
    user_id = message.from_user.id
    gcast_msg = await load_gcast_messages(user_id)

    send = message.reply_to_message
    if not send:
        return await message.edit("Balas ke pesan untuk melakukan spam.")

    interval = message.text.split()
    if len(interval) != 2 or not interval[1].isdigit():
        return await message.reply("Berikan jumlah spam dalam angka setelah perintah.")

    interval = int(interval[1])
    
    if client.me.is_premium:
        _proses = f"<emoji id={emot_proses}>🔸</emoji> {gcast_msg['proses']}"
    else:
        _proses = gcast_msg["proses"]
    
    await message.reply(_proses)

    if not send.text:
        return await message.edit("Tidak dapat mengirim pesan tanpa teks.")

    chats = await get_global_id(client, "group")
    blacklist = await get_chat(client.me.id)
    error = 0
    done = 0
    
    for _ in range(interval):
        for chat_id in chats:
            if chat_id in blacklist:
                continue
            if chat_id not in blgc:
                try:
                    await send.copy(chat_id)
                    done += 1
                    await asyncio.sleep(2)
                except FloodWait:
                    continue
                except SlowmodeWait:
                    continue
                except Exception:
                    continue
                except BaseException:
                    failed += 1

    await message.delete()

    if client.me.is_premium:
        _sukses = f"{gcast_msg['sukses']}\n<b><emoji id={emot_sukses}>✅</emoji></b> {done} group,\n<emoji id={emot_error}>❌</emoji> {error} group"
    else:
        _sukses = f"{gcast_msg['sukses']}\n✅ {done} ɢʀᴏᴜᴘ\n❌ {error} ɢʀᴏᴜᴘ"

    return await message.reply(_sukses)
