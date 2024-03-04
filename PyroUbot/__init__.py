import logging
import os
import re
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from pyrogram.types import Message
from pyromod import listen
from pytgcalls import GroupCallFactory
from PyroUbot.config import *
from PyroUbot.core.helpers.botlogs import izzy_meira, meira

SUDO_USERS = []
START_TIME = datetime.now()

class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for X in ["OSErro", "AuthKeyUnregistered"]:
            if X in record.getMessage():
                os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
connection_handler = ConnectionHandler()
logger.addHandler(stream_handler)
logger.addHandler(connection_handler)

class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, device_model="V1PremUbot")

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def on_callback_query(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(CallbackQueryHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()


class Ubot(Client):
    _ubot = []
    _prefix = {}
    _get_my_id = []
    _translate = {}
    _get_my_peer = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs, device_model="V2PremUbot")
        setattr(self, "group_call", GroupCallFactory(self).get_group_call())

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def set_prefix(self, user_id, prefix):
        self._prefix[user_id] = prefix

    async def get_prefix(self, user_id):
        return self._prefix.get(user_id, [".", ",", ":", ";", "!"])

    def cmd_prefix(self, cmd):
        command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

        async def func(_, client, message):
            if message.text:
                text = message.text.strip().encode("utf-8").decode("utf-8")
                username = client.me.username or ""
                prefixes = await self.get_prefix(client.me.id)

                if not text:
                    return False

                for prefix in prefixes:
                    if not text.startswith(prefix):
                        continue

                    without_prefix = text[len(prefix) :]

                    for command in cmd.split("|"):
                        if not re.match(
                            rf"^(?:{command}(?:@?{username})?)(?:\s|$)",
                            without_prefix,
                            flags=re.IGNORECASE | re.UNICODE,
                        ):
                            continue

                        without_command = re.sub(
                            rf"{command}(?:@?{username})?\s?",
                            "",
                            without_prefix,
                            count=1,
                            flags=re.IGNORECASE | re.UNICODE,
                        )
                        message.command = [command] + [
                            re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                            for m in command_re.finditer(without_command)
                        ]

                        return True

                return False

        return filters.create(func)

    async def start(self):
        await super().start()
        me = await self.get_me()
        handler = await get_pref(self.me.id)
        if handler:
            self._prefix[self.me.id] = handler
        else:
            self._prefix[self.me.id] = [".", ",", ":", ";", "!"]
        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = "id"
        #log = await meira(self)
        #if not log:
        #    try:
        #        group_name = "lancarjaya botlog"
        #        group_description = "lancarjaya botlog Group"
        #        await self.send_message("me", "Lancar Jaya userbot berhasil diaktifkan")
        #        await self.create_supergroup(group_name, group_description)
        #    except Exception as e:
        #        await self.send_message("me", f"gagal membuat group log, buat group log manual dengan nama group lancarjaya botlog, error : {e}")
        #        print(f"user {self.me.id} gagal membuat group log, error : {e}")
        #else:
        #    await self.send_message(log.id, "Lancar Jaya userbot berhasil diaktifkan")
        print(f"- ({me.id}) - STARTED")


bot = Bot(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

ubot = Ubot(name="ubot")


from PyroUbot.core.database import *
from PyroUbot.core.function import *
from PyroUbot.core.helpers import *
from PyroUbot.core.plugins import *
