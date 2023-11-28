import asyncio


async def del_cmd(client, message):
    rep = message.reply_to_message
    await message.delete()
    await rep.delete()


async def purgeme_cmd(client, message):
    if len(message.command) != 2:
        return await message.delete()
    n = (
        message.reply_to_message
        if message.reply_to_message
        else message.text.split(None, 1)[1].strip()
    )
    if not n.isnumeric():
        return await message.reply("ᴀʀɢᴜᴍᴇɴ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")
    n = int(n)
    if n < 1:
        return await message.reply("ʙᴜᴛᴜʜ ɴᴏᴍᴇʀ >=1-999")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user=int(message.from_user.id),
            limit=n,
        )
    ]
    if not message_ids:
        return await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    to_delete = [message_ids[i : i + 999] for i in range(0, len(message_ids), 999)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
        mmk = await message.reply(f"✅ {n} ᴘᴇsᴀɴ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
        await asyncio.sleep(2)
        await mmk.delete()


async def purge_cmd(client, message):
    await message.delete()
    if not message.reply_to_message:
        return await message.reply_text("ᴍᴇᴍʙᴀʟᴀs ᴘᴇsᴀɴ ᴜɴᴛᴜᴋ ᴅɪʙᴇʀsɪʜᴋᴀɴ.")
    chat_id = message.chat.id
    message_ids = []
    for message_id in range(
        message.reply_to_message.id,
        message.id,
    ):
        message_ids.append(message_id)
        if len(message_ids) == 100:
            await client.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,
            )
            message_ids = []
    if len(message_ids) > 0:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True,
        )
