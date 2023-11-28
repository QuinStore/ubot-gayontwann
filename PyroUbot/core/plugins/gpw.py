import random
import string

from pyrogram.enums import ParseMode


async def gen_password(client, message):
    if len(message.command) < 2:
        return await message.delete()
    try:
        count = int(message.command[1])
    except Exception as error:
        return await message.reply(str(error), quote=True)
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for x in range(count):
        password += random.choice(symbols)
    return await message.reply(password, parse_mode=ParseMode.MARKDOWN, quote=True)
