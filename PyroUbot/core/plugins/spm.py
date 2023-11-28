import asyncio


async def spam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs", quote=False)
    if reply:
        try:
            count_message = int(message.command[1])
            for i in range(count_message):
                await reply.copy(message.chat.id)
                await asyncio.sleep(0.1)
        except Exception as error:
            return await msg.edit(str(error))
    else:
        if len(message.command) < 2:
            return await msg.edit(
                "sɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ <code>.help spam</code> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ"
            )
        else:
            try:
                count_message = int(message.command[1])
                for i in range(count_message):
                    await message.reply(message.text.split(None, 2)[2], quote=False)
                    await asyncio.sleep(0.1)
            except Exception as error:
                return await msg.edit(str(error))
    await msg.delete()
    await message.delete()


async def dspam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs", quote=False)
    if reply:
        try:
            count_message = int(message.command[1])
            count_delay = int(message.command[2])
        except Exception as error:
            return await msg.edit(str(error))
        for i in range(count_message):
            try:
                await reply.copy(message.chat.id)
                await asyncio.sleep(count_delay)
            except:
                pass
    else:
        if len(message.command) < 4:
            return await msg.edit(
                "sɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ <code>.help spam</code> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ"
            )
        else:
            try:
                count_message = int(message.command[1])
                count_delay = int(message.command[2])
            except Exception as error:
                return await msg.edit(str(error))
            for i in range(count_message):
                try:
                    await message.reply(message.text.split(None, 3)[3], quote=False)
                    await asyncio.sleep(count_delay)
                except:
                    pass
    await msg.delete()
    await message.delete()
