from PyroUbot import *


__MODULE__ = "ʟᴏᴄᴋ"
__HELP__ = f"""
<b>『 bantuan untuk lockꜱ 』</b>

  <b>• perintah:</b> <code>.lock</code> [type]
  <b>• penjelasan:</b> untuk mengunci izin group

  <b>• perintah:</b> <code>.unlock</code> [type]
  <b>• penjelasan:</b> untuk membuka izin group

  <b>• perintah:</b> <code>.locks</code>
  <b>• penjelasan:</b> untuk melihat izin ꜱaat ini.

  <b>• type : `msg`|`media`|`stickers`|`polls`|`info`|`invite`|`webprev`|`pin`
"""


@PY.UBOT("lock|unlock")
async def _(client, message):
    await locks_func(client, message)


@PY.UBOT("locks")
async def _(client, message):
    await locktypes(client, message)
