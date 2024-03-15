import asyncio

from pyrogram import idle
from pyrogram.errors import *
from PyroUbot import *


start_msg = """
Juan Userbot sudah aktif

juanuserbot v3
"""

async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=60)
 
    except asyncio.TimeoutError:
        logger.info(f'[{ubot_.me.id}] - TimeoutError')
    except (
        AuthKeyDuplicated,
        AuthKeyUnregistered,
        SessionRevoked,
        Unauthorized,
        UserDeactivated,
        UserDeactivatedBan,
        ChannelPrivate
    ):
        await remove_ubot(user_id)
        session_file = f"{user_id}.session"
        if os.path.exists(session_file):
            os.remove(session_file)
            args = [sys.executable, "-m", "PyroUbot"]
            os.execle(sys.executable, *args, os.environ)


async def main():
    tasks = [
        asyncio.create_task(start_ubot(int(_ubot["name"]), _ubot))
        for _ubot in await get_userbots()
    ]
    await asyncio.gather(*tasks, bot.start())
    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots(), idle())


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
