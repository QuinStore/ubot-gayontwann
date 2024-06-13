__MODULE__ = "react"
__HELP__ = """
<b>『 bantuan untuk reaction 』</b>

  <b>• perintah:</b> <code>{0}react</code></code>
  <b>• penjelasan:</b> untuk memberikan reaction ke seluruh chat yang anda inginkan.
  
  
  <b>• perintah:</b> <code>{0}stopreact</code></code>
  <b>• penjelasan:</b> untuk menghentikan reaction.
  """

from PyroUbot import *
from pyrogram import Client, idle, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.types import ChatMember
from pyrogram.errors.exceptions import UserNotParticipant

reaction_progress = False

@PY.UBOT("react")
async def _(c, m):
    global reaction_progress
    reaction_progress = True
    try:
        if len(m.command) != 3:
            await m.reply("Mohon gunakan format: react username/id emoji")
            return

        chat_id = m.command[1]
    except IndexError:
        await m.reply("Mohon gunakan format: react username/id emoji")
        return

    rach = await m.reply("Processing..")
    async for message in c.get_chat_history(chat_id):
        await asyncio.sleep(0.5)
        chat_id = message.chat.id
        message_id = message.id
        try:
            if not reaction_progress:
                break
            await asyncio.sleep(0.5)
            await c.send_reaction(chat_id=chat_id, message_id=message_id, emoji=m.command[2])
        except Exception:
            pass
    
    await rach.edit(f"**Reaction telah selesai **✅")


@PY.UBOT("stopreact")
async def _(client, message):
    global reaction_progress
    reaction_progress = False
    await message.reply("Proses reaction telah dibatalkan.")
