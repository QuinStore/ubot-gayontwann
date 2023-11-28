import random

from pyrogram.types import InputMediaPhoto


async def pic_bing_cmd(client, message):
    TM = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    if len(message.command) < 2:
        return await TM.edit(f"<code>{message.text}</code> [ǫᴜᴇʀʏ]")
    x = await client.get_inline_bot_results(
        message.command[0], message.text.split(None, 1)[1]
    )
    get_media = []
    for X in range(4):
        try:
            saved = await client.send_inline_bot_result(
                client.me.id, x.query_id, x.results[random.randrange(len(x.results))].id
            )
            saved = await client.get_messages(
                client.me.id, int(saved.updates[1].message.id)
            )
            get_media.append(InputMediaPhoto(saved.photo.file_id))
            await saved.delete()
        except:
            pass
    if len(get_media) == 0:
        return await TM.edit("<b>❌ ɪᴍᴀɢᴇ ᴘʜᴏᴛᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    else:
        await client.send_media_group(
            message.chat.id,
            get_media,
            reply_to_message_id=message.id,
        )
        return await TM.delete()


async def gif_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(f"<code>{message.text}</code> [ǫᴜᴇʀʏ]")
    TM = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    try:
        x = await client.get_inline_bot_results(
            message.command[0], message.text.split(None, 1)[1]
        )
        saved = await client.send_inline_bot_result(
            client.me.id, x.query_id, x.results[random.randrange(len(x.results))].id
        )
    except:
        await message.reply("<b>❌ ɢɪꜰ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
        return await TM.delete()
    saved = await client.get_messages(client.me.id, int(saved.updates[1].message.id))
    await client.send_animation(
        message.chat.id, saved.animation.file_id, reply_to_message_id=message.id
    )
    await TM.delete()
    return await saved.delete()
