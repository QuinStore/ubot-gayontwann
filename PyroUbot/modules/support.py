from PyroUbot import *


@PY.CALLBACK("^support")
async def _(client, callback_query):
    await support_callback(client, callback_query)


@PY.CALLBACK("^jawab_pesan")
async def _(client, callback_query):
    await jawab_pesan_callback(client, callback_query)


@PY.CALLBACK("^profil")
async def _(client, callback_query):
    await profil_callback(client, callback_query)


@PY.CALLBACK("^batal")
async def _(client, callback_query):
    await batal_callback(client, callback_query)
