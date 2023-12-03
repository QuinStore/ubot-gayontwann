import asyncio
import imghdr
import os
import random
import shlex
from PIL import Image
from typing import Tuple
from pyrogram.errors import *
from pyrogram.raw.functions.messages import *
from pyrogram.raw.types import *
from pymediainfo import MediaInfo
from PyroUbot import *
from PyroUbot.core.plugins import *


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id


async def resize_media(media: str, video: bool, fast_forward: bool) -> str:
    if video:
        info_ = MediaInfo.parse(media)
        width = info_["pixel_sizes"][0]
        height = info_["pixel_sizes"][1]
        sec = info_["duration_in_ms"]
        s = round(float(sec)) / 1000

        if height == width:
            height, width = 512, 512
        elif height > width:
            height, width = 512, -1
        elif width > height:
            height, width = -1, 512

        resized_video = f"{media}.webm"
        if fast_forward:
            if s > 3:
                fract_ = 3 / s
                ff_f = round(fract_, 2)
                set_pts_ = ff_f - 0.01 if ff_f > fract_ else ff_f
                cmd_f = f"-filter:v 'setpts={set_pts_}*PTS',scale={width}:{height}"
            else:
                cmd_f = f"-filter:v scale={width}:{height}"
        else:
            cmd_f = f"-filter:v scale={width}:{height}"
        fps_ = float(info_["frame_rate"])
        fps_cmd = "-r 30 " if fps_ > 30 else ""
        cmd = f"ffmpeg -i {media} {cmd_f} -ss 00:00:00 -to 00:00:03 -an -c:v libvpx-vp9 {fps_cmd}-fs 256K {resized_video}"
        _, error, __, ___ = await run_cmd(cmd)
        os.remove(media)
        return resized_video

    image = Image.open(media)
    maxsize = 512
    scale = maxsize / max(image.width, image.height)
    new_size = (int(image.width * scale), int(image.height * scale))

    image = image.resize(new_size, Image.LANCZOS)
    resized_photo = "sticker.png"
    image.save(resized_photo)
    os.remove(media)
    return resized_photo

async def kang_cmd_bot(client: Client, message: Message):
    user = client.me
    replied = message.reply_to_message
    um = await message.edit_text("<code>ᴘʀᴏᴄᴇssɪɴɢ . . .</code>")
    media_ = None
    emoji_ = None
    is_anim = False
    is_video = False
    resize = False
    ff_vid = False
    if replied and replied.media:
        if replied.photo:
            resize = True
        elif replied.document and "image" in replied.document.mime_type:
            resize = True
            replied.document.file_name
        elif replied.document and "tgsticker" in replied.document.mime_type:
            is_anim = True
            replied.document.file_name
        elif replied.document and "video" in replied.document.mime_type:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.animation:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.video:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.sticker:
            if not replied.sticker.file_name:
                await um.edit("sᴛɪᴋᴇʀ ɪɴɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")
                return
            emoji_ = replied.sticker.emoji
            is_anim = replied.sticker.is_animated
            is_video = replied.sticker.is_video
            if not (
                replied.sticker.file_name.endswith(".tgs")
                or replied.sticker.file_name.endswith(".webm")
            ):
                resize = True
                ff_vid = True
        else:
            await um.edit("ғᴏʀᴍᴀᴛ ᴛɪᴅᴀᴋ ᴅɪᴅᴜᴋᴜɴɢ")
            return
        media_ = await client.download_media(replied, file_name="PyroUbot/resources/")
    else:
        await um.edit("ʙᴀʟᴀs ᴋᴇ sᴛɪᴋᴇʀ ᴀᴛᴀᴜ ᴍᴇᴅɪᴀ")
        return
    if media_:
        args = get_arg(message)
        pack = 1
        if len(args) == 2:
            emoji_, pack = args
        elif len(args) == 1:
            if args[0].isnumeric():
                pack = int(args[0])
            else:
                emoji_ = args[0]

        if emoji_ and emoji_ not in (
            getattr(emoji, _) for _ in dir(emoji) if not _.startswith("_")
        ):
            emoji_ = None
        if not emoji_:
            emoji_ = "✨"

        u_name = user.username
        u_name = "@" + u_name if u_name else user.first_name or user.id
        packname = f"Sticker_u{user.id}_v{pack}"
        custom_packnick = f"{u_name} Sticker Pack"
        packnick = f"{custom_packnick} Vol.{pack}"
        cmd = "/newpack"
        if resize:
            media_ = await resize_media(media_, is_video, ff_vid)
        if is_anim:
            packname += "_animated"
            packnick += " (Animated)"
            cmd = "/newanimated"
        if is_video:
            packname += "_video"
            packnick += " (Video)"
            cmd = "/newvideo"
        exist = False
        while True:
            try:
                exist = await client.invoke(
                    GetStickerSet(
                        stickerset=InputStickerSetShortName(short_name=packname), hash=0
                    )
                )
            except StickersetInvalid:
                exist = False
                break
            limit = 50 if (is_video or is_anim) else 120
            if exist.set.count >= limit:
                pack += 1
                packname = f"a{user.id}_by_lancarjaya_{pack}"
                packnick = f"{custom_packnick} Vol.{pack}"
                if is_anim:
                    packname += f"_anim{pack}"
                    packnick += f" (Animated){pack}"
                if is_video:
                    packname += f"_video{pack}"
                    packnick += f" (Video){pack}"
                await um.edit(
                    f"ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ, ᴋᴀʀᴇɴᴀ {pack} ᴛᴇʟᴀʜ ғᴜʟʟ"
                )
                continue
            break
        if exist is not False:
            try:
                await client.send_message("stickers", "/addsticker")
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            except Exception as e:
                return await client.edit(f"**ERROR:** `{e}`")
            await asyncio.sleep(2)
            await client.send_message("stickers", packname)
            await asyncio.sleep(2)
            limit = "50" if is_anim else "120"
            while limit in await get_response(message, client):
                pack += 1
                packname = f"a{user.id}_by_{user.username}_{pack}"
                packnick = f"{custom_packnick} vol.{pack}"
                if is_anim:
                    packname += "_anim"
                    packnick += " (Animated)"
                if is_video:
                    packname += "_video"
                    packnick += " (Video)"
                await um.edit(
                    "`Create a New Sticker Pack "
                    + str(pack)
                    + " Because the sticker pack is full`"
                )
                await client.send_message("stickers", packname)
                await asyncio.sleep(2)
                if await get_response(message, client) == "Invalid pack selected.":
                    await client.send_message("stickers", cmd)
                    await asyncio.sleep(2)
                    await client.send_message("stickers", packnick)
                    await asyncio.sleep(2)
                    await client.send_document("stickers", media_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", emoji_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", "/publish")
                    await asyncio.sleep(2)
                    if is_anim:
                        await client.send_message(
                            "Stickers", f"<{packnick}>", parse_mode=ParseMode.MARKDOWN
                        )
                        await asyncio.sleep(2)
                    await client.send_message("Stickers", "/skip")
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", packname)
                    await asyncio.sleep(2)
                    await um.edit(
                        f"sᴛɪᴄᴋᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪ ᴀᴍʙɪʟ\n**[CLICK HERE](https://t.me/addstickers/{packname})**"
                    )
                    return
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                await um.edit(
                    "ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ sᴛɪᴋᴇʀ, sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴍᴀɴᴜᴀʟ"
                )
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/done")
        else:
            await um.edit("`Create a New Sticker Pack`")
            try:
                await client.send_message("Stickers", cmd)
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packnick)
            await asyncio.sleep(2)
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                await um.edit(
                    "ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ sᴛɪᴋᴇʀ, sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴍᴀɴᴜᴀʟ"
                )
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/publish")
            await asyncio.sleep(2)
            if is_anim:
                await client.send_message("Stickers", f"<{packnick}>")
                await asyncio.sleep(2)
            await client.send_message("Stickers", "/skip")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packname)
            await asyncio.sleep(2)
        await um.edit(
            f"sᴛɪᴄᴋᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪ ᴀᴍʙɪʟ\n**[CLICK HERE](https://t.me/addstickers/{packname})**"
        )
        if os.path.exists(str(media_)):
            os.remove(media_)


async def get_response(message, client):
    return [x async for x in client.get_chat_history("Stickers", limit=1)][0].text


async def delete_results(msg, send, reply_send, results):
    for trash in (msg, send, reply_send, results):
        await trash.delete()


async def kang_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("<b>sɪʟᴀʜᴋᴀɴ ᴛᴜɴɢɢᴜ</b>")
    if message.reply_to_message:
        if reply.sticker or reply.photo or reply.animation:
            await client.unblock_user(bot.me.username)
            send = await reply.copy(bot.me.username)
            reply_send = await send.reply("/kang")
            await asyncio.sleep(5)
            results = await get_response(client, message)
            await results.copy(message.chat.id)
            return await delete_results(msg, send, reply_send, results)
        else:
            return await msg.edit("<b>ʜᴀʀᴀᴘ ʀᴇᴘʟʏ ᴋᴇ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ</b>")
    else:
        return await msg.edit("<b>ʜᴀʀᴀᴘ ʀᴇᴘʟʏ ᴋᴇ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ</b>")
