import os
from PyroUbot import *
from PyroUbot.core.function.emoji import emoji

async def create_grup(client, message):
    if len(message.command) < 3:
        return await message.reply(
            emoji("bintang") + f"**silahkan ketik** `{message.command}` **untuk melihat bantuan dari modul ini**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.reply(emoji("bintang") + f"**sedang memproses**...")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    try:
        if group_type == "gc":  # for supergroup
            _id = await client.create_supergroup(group_name, desc)
            link = await client.get_chat(_id.id)
            await xd.edit(
                f"<b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴜᴘ : [{group_name}]({link.invite_link})</b>" + emoji("bintang"),
                disable_web_page_preview=True,
            )
        elif group_type == "ch":  # for channel
            _id = await client.create_channel(group_name, desc)
            link = await client.get_chat(_id.id)
            await xd.edit(
                f"<b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ : [{group_name}]({link.invite_link})</b>" + emoji("bintang"),
                disable_web_page_preview=True,
            )
    except Exception as r:
        await xd.edit(emoji("bintang") + f"{r}")
