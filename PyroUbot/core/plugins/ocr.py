import requests
from telegraph import upload_file

from PyroUbot import *


async def read_cmd(client, message):
    reply = message.reply_to_message
    if not reply or not reply.photo and not reply.sticker and not reply.animation:
        return await message.reply_text(f"{message.text} ʀᴇᴘʟʏ ᴍᴇᴅɪᴀ")
    msg = await message.reply("ᴍᴇᴍʙᴀᴄᴀ ᴘᴇsᴀɴ ᴍᴇᴅɪᴀ....")
    try:
        file_path = await dl_pic(client, reply)
        response = upload_file(file_path)
        url = f"https://telegra.ph{response[0]}"
        req = requests.get(
            f"https://script.google.com/macros/s/AKfycbwURISN0wjazeJTMHTPAtxkrZTWTpsWIef5kxqVGoXqnrzdLdIQIfLO7jsR5OQ5GO16/exec?url={url}"
        ).json()
        await msg.edit(f"<code>{req['text']}</code>")
    except Exception as e:
        await msg.edit(str(e))
