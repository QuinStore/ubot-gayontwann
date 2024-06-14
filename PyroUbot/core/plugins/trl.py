import os
from gc import get_objects

import gtts
from gpytranslate import Translator
from pykeyboard import InlineKeyboard

from userbot import *


async def tts_cmd(client, message):
    TM = await message.reply("silahkan tunggu")
    if message.reply_to_message:
        language = client._translate[client.me.id]["negara"]
        words_to_say = message.reply_to_message.text or message.reply_to_message.caption
    else:
        if len(message.command) < 2:
            return await TM.edit(f"<code>{message.text}</code> reply/text")
        else:
            language = client._translate[client.me.id]["negara"]
            words_to_say = message.text.split(None, 1)[1]
    speech = gtts.gTTS(words_to_say, lang=language)
    speech.save("text_to_speech.oog")
    rep = message.reply_to_message or message
    try:
        await client.send_voice(
            chat_id=message.chat.id,
            voice="text_to_speech.oog",
            reply_to_message_id=rep.id,
        )
        await TM.delete()
    except Exception as error:
        await TM.edit(error)
    try:
        os.remove("text_to_speech.oog")
    except FileNotFoundError:
        pass


async def tr_cmd(client, message):
    try:
        trans = Translator()
        TM = await message.reply("silahkan tunggu")
        if message.reply_to_message:
            dest = client._translate[client.me.id]["negara"]
            to_translate = message.reply_to_message.text or message.reply_to_message.caption
            source = await trans.detect(to_translate)
        else:
            if len(message.command) < 2:
                return await message.reply(f"<code>{message.text}</code> reply/text")
            else:
               dest = client._translate[client.me.id]["negara"]
               to_translate = message.text.split(None, 1)[1]
               source = await trans.detect(to_translate)
        translation = await trans(to_translate, sourcelang=source, targetlang=dest)
        reply = f"<code>{translation.text}</code>"
        rep = message.reply_to_message or message
        await TM.delete()
        await client.send_message(message.chat.id, reply, reply_to_message_id=rep.id)
    except TypeError:
        await message.reply_text(f"mohon setting bahasa dulu ketik .bahasa")
    except Exception as r:
        await TM.delete()
        await message.reply_text(r)

async def set_lang_cmd(client, message):
    query = id(message)
    try:
        x = await client.get_inline_bot_results(bot.me.username, f"ubah_bahasa {query}")
        return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        return await message.reply(error)


async def ubah_bahasa_inline(client, inline_query):
    buttons = InlineKeyboard(row_width=3)
    keyboard = []
    for X in lang_code_translate:
        keyboard.append(
            InlineKeyboardButton(
                Fonts.smallcap(X.lower()),
                callback_data=f"set_bahasa {int(inline_query.query.split()[1])} {X}",
            )
        )
    buttons.add(*keyboard)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get bahasa!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(
                        "<b>• silahkan pilih bahasa translate</b>"
                    ),
                )
            )
        ],
    )


async def set_bahasa_callback(client, callback_query):
    data = callback_query.data.split()
    try:
        m = [obj for obj in get_objects() if id(obj) == int(data[1])][0]
        m._client._translate[m._client.me.id] = {"negara": lang_code_translate[data[2]]}
        return await callback_query.edit_message_text(
            f"<b>✅ berhasil diubah ke bahasa {Fonts.smallcap(data[2].lower())}"
        )
    except Exception as error:
        return await callback_query.edit_message_text(f"<code>{error}</code>")
