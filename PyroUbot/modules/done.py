import asyncio
import datetime
from PyroUbot import *

@PY.UBOT("done")
async def done_command(client, message):
    wannepep = await message.reply("memproses...")
    await asyncio.sleep(5)
    try:
        args = message.text.split(" ", 1)
        if len(args) < 2 or ',' not in args[1]:
            await message.reply_text("Penggunaan: .done <name item>,<price>,<payment>")
            return
        
        parts = args[1].split(",", 2)
        
        if len(parts) < 2:
            await message.reply_text("Penggunaan: .done <name item>,<price>,<payment>")
            return
        
        name_item = parts[0].strip()
        price = parts[1].strip()
        payment = parts[2].strip() if len(parts) > 2 else "Lainnya"        
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = (
            f"「 𝗧𝗥𝗔𝗡𝗦𝗔𝗞𝗦𝗜 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 」\n\n"
            f"📦 <b>Barang : {name_item}</b>\n"
            f"💸 <b>Nominal : {price}</b>\n"
            f"🕰️ <b>Waktu : {time}</b>\n"
            f"💬 <b>Payment : {payment}</b>\n\n"
            f"𝗧𝗲𝗿𝗶𝗺𝗮𝗸𝗮𝘀𝗶𝗵 𝗧𝗲𝗹𝗮𝗵 𝗢𝗿𝗱𝗲𝗿"
        )
        await wannepep.edit(response)
    
    except Exception as e:
        await wannepep.edit(f"error: {e}")
