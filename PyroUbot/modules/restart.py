from PyroUbot import *


@PY.BOT("login", FILTERS.OWNER)
@PY.UBOT("login", FILTERS.ME_OWNER)
async def _(client, message):
    await login_cmd(client, message)


@PY.BOT("restart")
async def _(client, message):
    await restart_cmd(client, message)
