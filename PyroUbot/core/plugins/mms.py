import random


async def memes_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("<code>memes</code> [ᴛᴇxᴛ]")
    try:
        text = f"#{random.randrange(67)} {message.text.split(None, 1)[1]}"
        TM = await message.reply("<code>ᴍᴇᴍᴘʀᴏsᴇs</code>")
        x = await client.get_inline_bot_results("StickerizerBot", text)
        saved = await client.send_inline_bot_result(
            client.me.id, x.query_id, x.results[0].id
        )
        saved = await client.get_messages(
            client.me.id, int(saved.updates[1].message.id)
        )
        await message.reply_sticker(saved.sticker.file_id, quote=True)
    except Exception as error:
        await message.reply(error, quote=True)
    await saved.delete()
    await TM.delete()
