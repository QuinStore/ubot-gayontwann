import asyncio
import datetime
from PyroUbot import *

__MODULE__ = "Done"
__HELP__ = """
 Bantuan Untuk Done

• Perintah : <code>{0}done</code> [name item] [harga] [pembayaran]
• Penjelasan : konfirmasi pembayaran.

"""
@PY.UBOT("done")
async def dunedun(client, message):
    pler = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
    await asyncio.sleep(3)
    try:
        args = message.text.split()
        if len(args) < 3:
            await message.reply_text("<b>Usage: .done <name item> <price> >payment<</b>")
            return
        
        name_item = args[1]
        price = args[2]
        payment = args[3]
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = (
            f"「 𝗧𝗥𝗔𝗡𝗦𝗔𝗞𝗦𝗜 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 」\n\n"
            f"📦 <b>Barang : {name_item}<b>\n"
            f"💸 <b>Nominal : {price}<b>\n"
            f"🕰️<b>Waktu : ${time}<b>\n"
            f"💬 <b>Payment : {payment}<b>\n\n"
            f"𝗧𝗲𝗿𝗶𝗺𝗮𝗸𝗮𝘀𝗶𝗵 𝗧𝗲𝗹𝗮𝗵 𝗢𝗿𝗱𝗲𝗿"
        )
        await pler.edit(response)
    
    except Exception as e:
        await pler.edit(f"An error occurred: {e}")
