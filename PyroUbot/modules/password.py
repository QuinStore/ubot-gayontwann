from PyroUbot import *


@PY.UBOT("pw")
async def _(client, message):
    await gen_password(client, message)
