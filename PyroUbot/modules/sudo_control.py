from pyrogram import filters
from PyroUbot import *
from PyroUbot.core.database.sudodb import add_sudos, get_sudos, remove_sudos

__MODULE__ = "sudo"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴜᴅᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addsudo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ sᴇʙᴀɢᴀɪ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}rmsudo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴɢʜᴀᴘᴜs ᴘᴇɴɢɢᴜɴᴀ sᴇʙᴀɢᴀɪ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}listsudo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇʟɪʜᴀᴛ ᴅᴀғᴛᴀʀ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ
  
  ᴘʀᴇғɪx : $
  ᴍᴏᴅᴜʟ sᴜᴅᴏ ʏᴀɴɢ ᴛᴇʀsᴇᴅɪᴀ:
    - ɢᴄᴀsᴛ
    - ғɢᴄᴀsᴛ
    - ʙɢᴄᴀsᴛ
    - ᴘɪɴɢ
    - ʟɪᴍɪᴛ
"""

@ubot.on_message(filters.command("gcast", "$"))
async def gcast_command_handler(client, message):
    user_id = message.from_user.id
    sudoers = await get_sudos(client.me.id)
    if user_id in sudoers:
        await broadcast_group_cmd(client, message)
    else:
        return

@ubot.on_message(filters.command("bgcast", "$"))
async def _(client, message):
    user_id = message.from_user.id
    sudoers = await get_sudos(client.me.id)
    if user_id in sudoers:
        await blue_gcast(client, message)
    else:
        return
   
@ubot.on_message(filters.command("limit", "$"))
async def _(client, message):
    user_id = message.from_user.id
    sudoers = await get_sudos(client.me.id)
    if user_id in sudoers:
        await limit_cmd(client, message)
    else:
        return

@ubot.on_message(filters.command("fgcast", "$"))
async def _(client, message):
    user_id = message.from_user.id
    sudoers = await get_sudos(client.me.id)
    if user_id in sudoers:
        await broadcast_cmd(client, message)
    else:
        return

@ubot.on_message(filters.command("ping", "$"))
async def _(client, message):
    usercrot = client.me.id
    user_id = message.from_user.id
    sudoers = await get_sudos(usercrot)
    if user_id in sudoers:
        await ping_cmd(client, message)
    else:
        return

@PY.UBOT("addsudo")
async def useradd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("ʙᴀʟᴀs ᴋᴇ ᴘᴇɴɢɢᴜɴᴀ.")

    sudo_user_id = message.reply_to_message.from_user.id
    umention = (await client.get_users(sudo_user_id)).mention
    user_id = message.from_user.id

    added = await add_sudos(user_id, sudo_user_id)
    if added:
        await message.edit(f"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ {umention} sᴇʙᴀɢᴀɪ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ\nʙᴏᴛ ʀᴇsᴛᴀʀᴛ !.")
        os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")
    else:
        await message.reply(f"{umention} sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ʟɪsᴛ sᴜᴅᴏ.")

@PY.UBOT("rmsudo")
async def rmsudo(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("ʙᴀʟᴀs ᴋᴇ ᴘᴇɴɢɢᴜɴᴀ.")
    sudo_user_id = message.reply_to_message.from_user.id
    umention = (await client.get_users(sudo_user_id)).mention
    user_id = message.from_user.id

    removed = await remove_sudos(user_id, sudo_user_id)
    if removed:
        await message.edit(f"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs {umention} ᴅᴀʀɪ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ.")
        os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")
    else:
        await message.reply(f"{umention} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅɪ ʟɪsᴛ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ.")

@PY.UBOT("listsudo")
async def sudo_list(client, message):
    sudousers = await get_sudos(client.me.id)
    oof = "ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ:\n"
    ex = await message.edit_text("ᴍᴇɴᴄᴀʀɪ")
    if len(sudousers) == 0:
        await ex.edit("ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
        return
    for lit in sudousers:
        user = await client.get_users(int(lit))
        oof += f"**ᴜsᴇʀ :** `{user.first_name}`\nᴜsᴇʀ ɪᴅ : `{user.id}` \n\n"
    return await ex.edit(oof)