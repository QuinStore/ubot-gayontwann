import asyncio

from pyrogram.errors import FloodWait

from PyroUbot import *

spam_taksdb = {}

kontol = False

__MODULE__ = "spam 2"
__HELP__ = """
 Bantuan Untuk Spam 2

• Perintah : <code>{0}sdspm</code> [Waktu] [Balas ke pesan]
• Penjelasan : Memulai spam ke database.

• Perintah : <code>{0}stdspm</code>
• Penjelasan : Menghentikan proses spam didatabase.

• Perintah : <code>{0}listspm</code> 
• Penjelasan : Melihat daftar grup didalam database.

• Perintah : <code>{0}addspm</code> 
• Penjelasan : Menambahkan grup ke dalam database spam.

• Perintah : <code>{0}delspm</code> 
• Penjelasan : Menghapus grup dari database spam.
"""


@PY.UBOT("sdspm")
async def _(c, m):
    global kontol

    if not m.reply_to_message:
        return await m.reply("<b>Silakan balas ke pesan !!</b>")
    if len(m.command) != 2:
        return await m.reply("<b>Silahkan balas ke pesan dan berikan waktu delay.</b>")
    try:
        interval = int(m.command[1])
    except ValueError:
        return await m.reply("<b>Waktu delay harus berupa angka.</b>")

    scheduled_message = m.reply_to_message
    chat_ids = monggo.ambil_spdb(c.me.id)
    kontol = True
    for chat_id in chat_ids:
        if not kontol:
            break
        if interval < 10:
            await m.reply(
                f"<b>Minimal waktu delay 10 jangan  <code>{interval}</code></b>"
            )
        else:

            async def send_scheduled_message(chat_id):
                try:
                    while True:
                        await asyncio.sleep(interval)
                        await scheduled_message.copy(chat_id)
                except FloodWait:
                    if chat_id in spam_taksdb:
                        task = spam_taksdb[chat_id]
                        task.cancel()
                        del spam_taksdb[chat_id]

            task = asyncio.create_task(send_scheduled_message(chat_id))
            spam_taksdb[chat_id] = task
    kontol = False
    await m.reply(f"<b>Processing Spam To Database !</b>")


@PY.UBOT("stdspm")
async def _(c, m):
    global kontol
    if not kontol:
        return await m.reply_text(
            "<b>Tidak ada pengiriman spam yang sedang berlangsung.</b>"
        )
    chat_ids = monggo.ambil_spdb(c.me.id)
    for chat_id in chat_ids:
        if chat_id in spam_taksdb:
            task = spam_taksdb[chat_id]
            task.cancel()
            del spam_taksdb[chat_id]
    kontol = False
    await m.reply("<b>Spam database dihentikan.</b>")


@PY.UBOT("listspm")
async def _(c, m):
    teks = "<b>Daftar Database Spam:</b>\n\n"
    user_id = c.me.id
    lists = monggo.ambil_spdb(user_id)
    if len(lists) == 0:
        await m.reply("<b>Database kosong.</b>")
    else:
        for count, chat_id in enumerate(lists, 1):
            teks += f"{count}. <code>{chat_id}</code>\n"
        await m.reply(teks)


@PY.UBOT("addspm|delspm")
async def _(c, m):
    user_id = c.me.id
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    mmk = await m.reply("<b>Processing...</b>")
    if m.command[0] == "addspm":
        monggo.tambah_spdb(user_id, chat_id)
        return await mmk.edit(
            f"<code>{chat_id}</code> <b>Berhasil di tambahkan ke database.</b>"
        )
    elif m.command[0] == "delspm":
        monggo.kureng_spdb(user_id, chat_id)
        return await mmk.edit(
            f"<code>{chat_id}</code> <b>Berhasil di hapus dari database.</b>"
        )
    else:
        return await mmk.edit(f"<b>Silakan ketik <code>{m.text}.</code></b>")
