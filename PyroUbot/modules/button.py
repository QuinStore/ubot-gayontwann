from gc import get_objects
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from PyroUbot import *

__MODULE__ = "button"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴜᴛᴛᴏɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}button</code> ᴛᴇxᴛ ~> ʙᴜᴛᴛᴏɴ_ᴛᴇxᴛ:ʙᴜᴛᴛᴏɴ_ʟɪɴᴋ
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴏᴍʙᴏʟ ɪɴʟɪɴᴇ - ᴍᴀxɪᴍᴀʟ 100 ʙᴜᴛᴛᴏɴ
"""


@PY.UBOT("button")
async def cmd_button(client, message):
    if len(message.command) < 2:
        return await message.reply(f"{message.text} text ~> button_name:link_url")
    if "~>" not in message.text:
        return await message.reply(
            "sɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ <code>.help button</code> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ"
        )
    await message.delete()
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"get_button {id(message)}"
        )
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[0].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)


@PY.INLINE("^get_button")
@INLINE.QUERY
async def inline_button(client, inline_query):
    get_id = int(inline_query.query.split(None, 1)[1])
    m = [obj for obj in get_objects() if id(obj) == get_id][0]
    buttons, text = await create_button(m)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get button!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(text),
                )
            )
        ],
    )
