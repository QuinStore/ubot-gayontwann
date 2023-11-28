from pyrogram import Client
from pyrogram.types import Message
from PyroUbot import *
from PyroUbot.core.database.sudodb import add_sudo, remove_sudo, get_sudo

@PY.UBOT("addsudo")
async def useradd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("ʙᴀʟᴀs ᴋᴇ ᴘᴇɴɢɢᴜɴᴀ.")

    user_id = message.reply_to_message.from_user.id
    umention = (await client.get_users(user_id)).mention
    sudoers = await get_sudo(user_id)

    if user_id in sudoers:
        return await message.edit(f"{umention} sᴜᴅᴀʜ ᴛᴇʀᴅᴀғᴛᴀʀ sᴇʙᴀɢᴀɪ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ.")

    sudoers.append(user_id)
    await add_sudo(user_id)

    if user_id not in SUDO_USERS:
        SUDO_USERS.append(user_id)

    await message.edit(f"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ {umention} sᴇʙᴀɢᴀɪ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ.")

@PY.UBOT("rmsudo")
async def rmsudo(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("ʙᴀʟᴀs ᴋᴇ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ.")
    user_id = message.reply_to_message.from_user.id
    umention = (await client.get_users(user_id)).mention

    if user_id not in await get_sudo(user_id):
        return await message.edit(f"{umention} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅɪ ʟɪsᴛ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ.")

    await remove_sudo(user_id)

    if user_id in SUDO_USERS:
        SUDO_USERS.remove(user_id)

    await message.edit(f"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs {umention} ᴅᴀʀɪ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ.")

@PY.UBOT("listsudo")
async def gbanlist(client: Client, message: Message):
    users = await get_sudo(client.me.id)
    oof = "ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ:\n"
    ex = await message.edit_text("`mencari...`")
    if len(users) == 0:
        await ex.edit("ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
        return
    for lit in users:
        user = await client.get_users(int(lit))
        oof += f"**ᴜsᴇʀ :** `{user.first_name}`\nᴜsᴇʀ ɪᴅ : `{user.id}` \n\n"
    return await ex.edit(oof)

