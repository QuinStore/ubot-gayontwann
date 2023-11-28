import asyncio
import os

import requests
from bs4 import BeautifulSoup


def qr_gen(content):
    return {
        "data": content,
        "config": {
            "body": "circle-zebra",
            "eye": "frame13",
            "eyeBall": "ball14",
            "erf1": [],
            "erf2": [],
            "erf3": [],
            "brf1": [],
            "brf2": [],
            "brf3": [],
            "bodyColor": "#000000",
            "bgColor": "#FFFFFF",
            "eye1Color": "#000000",
            "eye2Color": "#000000",
            "eye3Color": "#000000",
            "eyeBall1Color": "#000000",
            "eyeBall2Color": "#000000",
            "eyeBall3Color": "#000000",
            "gradientColor1": "",
            "gradientColor2": "",
            "gradientType": "linear",
            "gradientOnEyes": "true",
            "logo": "",
            "logoMode": "default",
        },
        "size": 1000,
        "download": "imageUrl",
        "file": "png",
    }


async def qr_gen_cmd(client, message):
    ID = message.reply_to_message or message
    if message.reply_to_message:
        data = qr_gen(message.reply_to_message.text)
    else:
        if len(message.command) < 2:
            return await message.delete()
        else:
            data = qr_gen(message.text.split(None, 1)[1])
    Tm = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ʙᴜᴀᴛ ǫʀᴄᴏᴅᴇ....")
    try:
        QRcode = (
            requests.post(
                "https://api.qrcode-monkey.com//qr/custom",
                json=data,
            )
            .json()["imageUrl"]
            .replace("//api", "https://api")
        )
        await client.send_photo(message.chat.id, QRcode, reply_to_message_id=ID.id)
        await Tm.delete()
    except Exception as error:
        await Tm.edit(error)


async def qr_read_cmd(client, message):
    replied = message.reply_to_message
    if not (replied and replied.media and (replied.photo or replied.sticker)):
        await message.reply("ʙᴀʟᴀs ᴋᴏᴅᴇ ǫʀ ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀᴛᴀ...")
        return
    if not os.path.isdir("premiumQR/"):
        os.makedirs("premiumQR/")
    AM = await message.reply("ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴇᴅɪᴀ...")
    down_load = await client.download_media(message=replied, file_name="premiumQR/")
    await AM.edit("ᴍᴇᴍᴘʀᴏsᴇs ᴋᴏᴅᴇ ǫʀ ᴀɴᴅᴀ...")
    cmd = [
        "curl",
        "-X",
        "POST",
        "-F",
        "f=@" + down_load + "",
        "https://zxing.org/w/decode",
    ]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    out_response = stdout.decode().strip()
    err_response = stderr.decode().strip()
    os.remove(down_load)
    if not (out_response or err_response):
        await AM.edit("ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀᴛᴀ ᴋᴏᴅᴇ ǫʀ ɪɴɪ...")
        return
    try:
        soup = BeautifulSoup(out_response, "html.parser")
        qr_contents = soup.find_all("pre")[0].text
    except IndexError:
        await AM.edit("ɪɴᴅᴇᴋs ᴅᴀꜰᴛᴀʀ ᴅɪ ʟᴜᴀʀ ᴊᴀɴɢᴋᴀᴜᴀɴ")
        return
    await AM.edit(f"<b>ᴅᴀᴛᴀ ǫʀᴄᴏᴅᴇ:</b>\n<code>{qr_contents}</code>")
