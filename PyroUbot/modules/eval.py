from PyroUbot import *
from pyrogram import filters
from random import randint
DEVS = [924769291, 1998135373]



@PY.BOT("sh", FILTERS.OWNER)
@PY.UBOT("sh", FILTERS.ME_OWNER)
async def _(client, message):
    await shell_cmd(client, message)


@PY.BOT("eval", FILTERS.OWNER)
@PY.UBOT("eval", FILTERS.ME_OWNER)
async def _(client, message):
    await evalator_cmd(client, message)


@PY.UBOT("trash")
async def _(client, message):
    await trash_cmd(client, message)


@PY.UBOT("getotp|getnum", FILTERS.ME_OWNER)
async def _(client, message):
    await get_my_otp(client, message)


@PY.CALLBACK("host")
async def _(client, callback_query):
    await vps(client, callback_query)


    
