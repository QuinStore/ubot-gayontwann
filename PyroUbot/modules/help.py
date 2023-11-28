from PyroUbot import *


@PY.UBOT("help")
async def _(client, message):
    await help_cmd(client, message)


@PY.INLINE("^user_help")
@INLINE.QUERY
async def _(client, inline_query):
    await menu_inline(client, inline_query)


@PY.CALLBACK("help_(.*?)")
# @INLINE.DATA
async def _(client, callback_query):
    try:
        await menu_callback(client, callback_query)
    except:
        pass
