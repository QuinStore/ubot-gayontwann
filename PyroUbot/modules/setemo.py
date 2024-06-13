from PyroUbot import *
from pyrogram.types import EmojiStatus, MessageEntity
from pyrogram.enums import MessageEntityType

__MODULE__ = "ꜱᴇᴛᴇᴍᴏ"
__HELP__ = f"""
<b>『 bantuan untuk setemo 』</b>

  <b>• perintah:</b> <code>.setemo</code> [reply to user - text]
  <b>• penjelasan:</b> untuk mengganti emoji status

"""

@PY.UBOT("setemo")
async def _(client, message):
    try:
        target = message.reply_to_message
        if not target:
            await message.reply_text(f"<emoji id=5911461474315802019>⭐</emoji> **mohon balas ke pesan** !", quote=True)
            return
        entity = target.entities[0]
        custom_emoji_id = entity.custom_emoji_id
        chat_id = message.chat.id
        success = await client.set_emoji_status(EmojiStatus(custom_emoji_id=custom_emoji_id))
        if success:
            my_emoji_str = f"**emoji status berhasil di ganti ke** <emoji id={custom_emoji_id}>{target.text}</emoji>"
            await message.reply_text(my_emoji_str, quote=True)
                    
    except Exception as e:
        await message.reply_text(e)
