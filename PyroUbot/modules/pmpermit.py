from pyrogram import filters, Client, enums
from pyrogram.types import Message
from PyroUbot.core.database import set_vars, get_vars, remove_all_vars
from PyroUbot.core.database.pmpermitdb import check_user_approved, add_approved_user, rm_approved_user
from PyroUbot import *

PM_GUARD_WARNS_DB = {}
PM_GUARD_MSGS_DB = {}

DEFAULT_TEXT = """
Saya adalah Userbot yang menjaga Room Chat Ini . Jangan Spam Atau Anda Akan Diblokir Otomatis.
"""

PM_WARN = """
Halo  {} 👋 .
Pesan Keamanan Milik {} 👮!**

{}

**Anda memiliki `{}/{}` peringatan . Hati-hati !
"""

LIMIT = 5

class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()

@PY.UBOT("permiton")
async def permitpm_on(client, message):
    user_id = client.me.id
    msg = await message.reply("`Processing...`")

    is_already = await get_vars(user_id, "ENABLE_PM_GUARD")
    if is_already:
        return await msg.edit("`PMPermit Sudah DiHidupkan.`")
    else:
        await set_vars(user_id, "ENABLE_PM_GUARD", True)
        await msg.edit("**PMPermit Berhasil DiHidupkan.**")

@PY.UBOT("permitoff")
async def permitpm_off(client, message):
    user_id = client.me.id
    msg = await message.reply("`Processing...`")
    
    is_already = await get_vars(user_id, "ENABLE_PM_GUARD")
    if not is_already:
        return await msg.edit("`PMPermit Sudah Dimatikan.`")
    else:
        await set_vars(user_id, "ENABLE_PM_GUARD", False)
        await msg.edit("**PMPermit Berhasil Dimatikan.**")

@PY.UBOT("ok")
async def approve(client, message):
    msg = await message.reply("`Processing...`")
    chat_type = message.chat.type
    if chat_type == "me":
        return await msg.edit("`haaa ?`")
    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not message.reply_to_message.from_user:
            return await msg.edit("`Balas ke pesan pengguna, untuk disetujui.`")
        user_id = message.reply_to_message.from_user.id
    elif chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
    else:
        return
    already_apprvd = await check_user_approved(user_id)
    if already_apprvd:
        return await msg.edit("`Pengguna sudah Di Setujui Untuk mengirim pesan.`")
    await add_approved_user(user_id)
    if user_id in PM_GUARD_WARNS_DB:
        PM_GUARD_WARNS_DB.pop(user_id)
        try:
            await client.delete_messages(
                chat_id=user_id, message_ids=PM_GUARD_MSGS_DB[user_id]
            )
        except:
            pass
    await msg.edit("**Baiklah, pengguna ini sudah disetujui untuk mengirim pesan.**")

@PY.UBOT("no")
async def disapprove(client, message):
    msg = await message.reply("`Processing...`")
    chat_type = message.chat.type
    if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not message.reply_to_message.from_user:
            return await msg.edit("`Balas ke pesan pengguna, untuk ditolak.`")
        user_id = message.reply_to_message.from_user.id
    elif chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
    else:
        return
    already_apprvd = await check_user_approved(user_id)
    if not already_apprvd:
        return await msg.edit(
            "`Penggguna belum Di Setujui Untuk mengirim pesan.`"
        )
    await rm_approved_user(user_id)
    await msg.edit("**Pengguna ini ditolak untuk mengirim pesan.**")

@PY.UBOT("setmsg")
async def set_msg(client, message):
    msg = await message.reply("`Processing...`")
    user_id = client.me.id
    r_msg = message.reply_to_message
    args_txt = get_arg(message)
    if r_msg:
        if r_msg.text:
            pm_txt = r_msg.text
        else:
            return await msg.edit(
                "`Silakan balas ke pesan untuk dijadikan teks PMPermit !`"
            )
    elif args_txt:
        pm_txt = args_txt
    else:
        return await msg.edit(
            "`Silakan balas ke pesan atau berikan pesan untuk dijadikan teks PMPermit !\n**Contoh :** .setmsg Halo saya GAY`"
        )
    await set_vars(user_id, "CUSTOM_PM_TEXT", pm_txt)
    await msg.edit(f"**PMPemit berhasil diatur menjadi : `{pm_txt}`.**")

@PY.UBOT("setlimit")
async def set_limit(client, message):
    msg = await message.reply("`Processing...`")
    user_id = client.me.id
    args_txt = get_arg(message)
    if args_txt:
        if args_txt.isnumeric():
            pm_warns = int(args_txt)
        else:
            return await msg.edit("`Silakan berikan untuk angka!`")
    else:
        return await msg.edit(
            "`Silakan berikan angka!\n**Contoh :** .setlimit 5`"
        )
    await set_vars(user_id, "CUSTOM_PM_WARNS_LIMIT", pm_warns)
    await msg.edit(f"**Pesan Limit berhasil diatur menjadi : `{args_txt}`.**")


@ubot.on_message(
    filters.private & filters.incoming & ~filters.service & ~filters.me & ~filters.bot,
    group=69,
)
async def handle_pmpermit(client, message):
    user_id = client.me.id
    siapa = message.from_user.id
    biji = message.from_user.mention
    chat_id = message.chat.id
    group = await izzy_meira(client)
    if not group:
        await meira(client)
    is_pm_guard_enabled = await get_vars(user_id, "ENABLE_PM_GUARD")
    if message.chat.id != 777000:
        if LOG_CHATS_.RECENT_USER != message.chat.id:
            LOG_CHATS_.RECENT_USER = message.chat.id
            if LOG_CHATS_.NEWPM:
                await LOG_CHATS_.NEWPM.edit(
                    LOG_CHATS_.NEWPM.text.replace(
                        "**💌 #NEW_MESSAGE**",
                        f" • `{LOG_CHATS_.COUNT}` **Pesan**",
                    )
                )
                LOG_CHATS_.COUNT = 0
            LOG_CHATS_.NEWPM = await client.send_message(
                group.id,
                f"💌  <u>MENERUSKAN PESAN BARU</u> \n  • Dari :  {biji}\n  • User ID :   **{siapa} **\n",
                parse_mode=enums.ParseMode.HTML,
            )
        try:
            async for pmlog in client.search_messages(message.chat.id, limit=1):
                await pmlog.forward(group.id)
            LOG_CHATS_.COUNT += 1
        except BaseException:
            pass
    if not is_pm_guard_enabled:
        return
    in_user = message.from_user
    is_approved = await check_user_approved(in_user.id)
    if is_approved:
        return
    elif in_user.is_fake or in_user.is_scam:
        await message.reply("`Sepertinya anda mencurigakan...`")
        return await client.block_user(in_user.id)
    elif in_user.is_support or in_user.is_verified or in_user.is_self:
        return
    #elif siapa in OWNER_ID:
    #    try:
    #        await add_approved_user(chat_id)
    #        await client.send_message(
    #            chat_id,
    #            f"Menerima Pesan Dari {biji} !!\nTerdeteksi Developer Dari Userbot.",
    #            parse_mode=enums.ParseMode.HTML,
    #        )
    #    except:
    #        pass
     #   return
    master = await client.get_me()
    getc_pm_txt = await get_vars(user_id, "CUSTOM_PM_TEXT")
    getc_pm_warns = await get_vars(user_id, "CUSTOM_PM_WARNS_LIMIT")
    custom_pm_txt = getc_pm_txt if getc_pm_txt else DEFAULT_TEXT
    custom_pm_warns = getc_pm_warns if getc_pm_warns else LIMIT
    if in_user.id in PM_GUARD_WARNS_DB:
        try:
            if message.chat.id in PM_GUARD_MSGS_DB:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=PM_GUARD_MSGS_DB[message.chat.id],
                )
        except:
            pass
        PM_GUARD_WARNS_DB[in_user.id] += 1
        if PM_GUARD_WARNS_DB[in_user.id] >= custom_pm_warns:
            await message.reply(
                f"`Saya sudah memberi tahu peringatan {custom_pm_warns}\nTunggu tuan saya menyetujui pesan anda, atau anda akan diblokir !`"
            )
            return await client.block_user(in_user.id)
        else:
            rplied_msg = await message.reply(
                PM_WARN.format(
                    biji,
                    master.mention,
                    custom_pm_txt,
                    PM_GUARD_WARNS_DB[in_user.id],
                    custom_pm_warns,
                )
            )
    else:
        PM_GUARD_WARNS_DB[in_user.id] = 1
        rplied_msg = await message.reply(
            PM_WARN.format(
                biji,
                master.mention,
                custom_pm_txt,
                PM_GUARD_WARNS_DB[in_user.id],
                custom_pm_warns,
            )
        )
    PM_GUARD_MSGS_DB[message.chat.id] = [rplied_msg.id]

__MODULE__ = "pm permit"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}permiton</code> 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴘᴍ ᴘᴇʀᴍɪᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}permitoff</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴘᴍ ᴘᴇʀᴍɪᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ok</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴᴇʀɪᴍᴀ ᴘᴇsᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}no</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴᴏʟᴀᴋ ᴘᴇsᴀɴ ᴅᴀɴ ʙʟᴏᴋɪʀ ᴘᴇɴɢɢᴜɴᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setmsg</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴɢᴀᴛᴜʀ ᴘᴇsᴀɴ ᴘᴍ ᴘᴇʀᴍɪᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setmsg</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴍᴇɴɢᴀᴛᴜʀ ʟɪᴍɪᴛ ᴘᴍ ᴘᴇʀᴍɪᴛ
"""