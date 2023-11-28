from PyroUbot import *


@PY.UBOT("alive")
async def _(client, message):
    await alive_cmd(client, message)


@PY.INLINE("^alive")
@INLINE.QUERY
async def _(client, inline_query):
    await alive_query(client, inline_query)


@PY.CALLBACK("alv_cls")
@INLINE.DATA
async def _(client, callback_query):
    await alive_close(client, callback_query)
