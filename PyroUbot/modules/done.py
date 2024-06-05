import asyncio
import datetime
from PyroUbot import *

@PY.UBOT("done")
async def dunedun(client, message):
    pler = await message.reply("silahkan tunggu...")
    await asyncio.sleep(3)
    try:
        args = message.text.split()
        if len(args) < 3:
            await message.reply_text("Usage: .done <name item> <price>")
            return
        
        name_item = args[1]
        price = args[2]
        payment = args[3]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = (
            f"payment done\n\n"
            f"name item: {name_item}\n"
            f"date: {now}\n"
            f"price: {price}\n"
            f"payment: {payment}"
        )
        await pler.edit(response)
    
    except Exception as e:
        await pler.edit(f"An error occurred: {e}")
