import datetime
from PyroUbot import *

@PY.UBOT("done")
async def done_command(message):
    try:
        args = message.text.split()
        if len(args) < 3:
            message.reply_text("Usage: .done <name item> <price>")
            return
        
        name_item = args[1]
        price = args[2]
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = (
            f"payment done\n\n"
            f"name item: {name_item}\n"
            f"date: {now}\n"
            f"price: {price}\n"
            f"payment: Optional"
        )
        message.reply_text(response)
    
    except Exception as e:
        message.reply_text(f"An error occurred: {e}")