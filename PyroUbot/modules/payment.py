from PyroUbot import *


@PY.CALLBACK("^confirm")
async def _(client, callback_query):
    await confirm_callback(client, callback_query)


@PY.CALLBACK("^(kurang|tambah)")
async def _(client, callback_query):
    await tambah_or_kurang(client, callback_query)


@PY.CALLBACK("^(success|failed|home)")
async def _(client, callback_query):
    await success_failed_home_callback(client, callback_query)
