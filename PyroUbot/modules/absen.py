__MODULE__ = "absen"
__HELP__ = """
<b>『 bantuan untuk absen 』</b>

  <b>• perintah:</b> <code>{0}absen</code></code>
  <b>• penjelasan:</b> untuk membuat list absen kamu.
  
  
  <b>• perintah:</b> <code>{0}delabsen</code></code>
  <b>• penjelasan:</b> untuk menghapus list absen kamu.
  """

from PyroUbot import *

@PY.UBOT("absen")
async def _(client, message):
    await absen_command(client, message)
    
    
@PY.UBOT("delabsen")
async def _(client, message):
    await clear_absen_command(client, message)


@PY.INLINE("^absen_in")
async def _(client, inline_query):
    await absen_query(client, inline_query)

@PY.CALLBACK("absen_hadir")
async def _(client, callback_query):
        await hadir_callback(client, callback_query)


