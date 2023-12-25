from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from PyroUbot import *
from PyroUbot.core.helpers.tools import get_arg

DEV = [1998135373, 6619405249, 874946835]

__MODULE__ = "vctools"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟs』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}joinvc</code> 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴊᴏɪɴ ᴠᴄɢ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leavevc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴠᴄɢ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}startvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇᴍᴜʟᴀɪ ᴠᴄɢ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stopvc</code> 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴɢᴀᴋʜɪʀɪ ᴠᴄɢ
"""

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.send(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.reply(f"ᴠᴄɢ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ {err_msg}")
    return False

@ubot.on_message(filters.command("jvc", ".") & filters.user(DEV))
@PY.UBOT("joinvc")
async def joinvc(client: Client, message: Message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        meira = await message.reply("ᴍᴇᴍᴘʀᴏsᴇss...")
    else:
        meira = await message.edit("ᴍᴇᴍᴘʀᴏsᴇss...")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.start(chat_id)
    except Exception as e:
        return await meira.edit(f"ᴇʀʀᴏʀ `{e}`")
    await meira.edit(f"▢ <b>ʙᴇʀʜᴀsɪʟ ᴊᴏɪɴ ᴠᴄɢ</b>\n<b>ᴄʜᴀᴛ :</b><code>{chat_id}</code>")
    await sleep(3)
    await client.group_call.set_is_mute(True)
    await sleep(1)
    await meira.delete()

@ubot.on_message(filters.command("lvc", ".") & filters.user(DEV))
@PY.UBOT("leavevc")
async def leavevc(client: Client, message: Message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        meira = await message.reply("ᴍᴇᴍᴘʀᴏsᴇss...")
    else:
        meira = await message.edit("ᴍᴇᴍᴘʀᴏsᴇss...")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.stop()
    except Exception as e:
        return await meira.edit(message, f"**ERROR:** `{e}`")
    msg = (f"▢ <b>ʙᴇʀʜᴀsɪʟ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ</b>\n<b>ᴄʜᴀᴛ :</b><code>{chat_id}</code>")
    await meira.edit(msg)
    await sleep(3)
    await meira.delete(msg)

@PY.UBOT("startvc")
async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    meira = await message.edit("ᴍᴇᴍᴘʀᴏsᴇss...")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"<b>ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>\n • <b>ᴄʜᴀᴛ</b> : {message.chat.title}"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>ᴛɪᴛʟᴇ:</b> {vctitle}"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await meira.edit(args)
    except Exception as e:
        await meira.edit(f"<b>ɪɴғᴏ:</b> `{e}`")

@PY.UBOT("stopvc")
async def end_vc_(client: Client, message: Message):
    meira = await message.edit("ᴘʀᴏᴄᴇssɪɴɢ...")
    message.chat.id
    if not (
        group_call := (await get_group_call(client, message, err_msg=", ᴇʀʀᴏʀ!"))
    ):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await meira.edit(
        f"<b>ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ᴅɪʜᴇɴᴛɪᴋᴀɴ</b>\n • <b>ᴄʜᴀᴛ</b> : {message.chat.title}"
    )