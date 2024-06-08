from PyroUbot import *

__MODULE__ = "Download"
__HELP__ = """
 <b>Bantuan Untuk Done</b>

• <b>Perintah</b> : <code>{0}tiktok</code> <b>[Link tiktok]</b>
• <b>Penjelasan : Download Vt Tiktok No Wm</b>

"""
@PY.UBOT("tiktok")
async def _(client, message):
    
     await message.edit("```Video Sedang Diproses.....```")
    chat = "@ttsavebot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await message.edit("**Kesalahan:** `Mohon Buka Blokir` @ttsavebot `Dan Coba Lagi !`")
            return
        await bot.send_file(message.chat_id, video)
        await message.client.delete_messages(conv.chat_id,
                                           [msg_start.id, r.id, msg.id, details.id, video.id])
        await message.delete()
