from time import time
from pyrogram import Client, filters
from random import randint
from .. import *
from PyroUbot import *
DEV = [1998135373, 6619405249, 874946835]

TIME_DURATION_UNITS = (
    ("w", 60 * 60 * 24 * 7),
    ("d", 60 * 60 * 24),
    ("h", 60 * 60),
    ("m", 60),
    ("s", 1),
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount}{unit}{"" if amount == 1 else ""}')
    return ":".join(parts)


#@ubot.on_message(filters.command("cping", ".") & filters.user(DEV))
@PY.UBOT("ping")
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)

@ubot.on_message(filters.command("cping", ".") & filters.user(DEV))
async def cping(client, message):
    start = time()
    current_time = datetime.now()
    await client.invoke(Ping(ping_id=randint(0, 2147483647)))
    delta_ping = round((time() - start) * 1000, 3)
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    _ping = f"""
    <b>pong</b>🏓
<i> Ping:</i> `{delta_ping} ms`
"""
    await message.reply(_ping)
    await asyncio.sleep(10)
    await message.delete()

#@ubot.on_message(filters.regex(r'\btest\b', re.IGNORECASE) & filters.user(DEV))
#async def test_dev(client: Client, message):
#    emot={"🤩","😭","🥳","🥰","😘","😡","😢","😅","😏","😝","🤤","😍","🥵",}
#    await client.send_reaction(random.choice(emot))
