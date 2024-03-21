import json
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from PyroUbot.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.pyro_ubot

class MongoDB:
    def __init__(self, db_name, mongo_url: str) -> None:
        self._db = MongoClient(mongo_url)
        self._db = self._db[db_name]

    def ambil_spgc(self, user_id):
        spam_gc = self._db.spam_gc

        result = spam_gc.find_one({"user_id": user_id}, {"_id": 0, "chat_id": 1})

        return json.loads(result["chat_id"]) if result and "chat_id" in result else []

    def tambah_spgc(self, user_id, chat_id):
        spam_gc = self._db.spam_gc

        current_list = self.ambil_spgc(user_id)
        current_list.append(chat_id)

        spam_gc.update_one(
            {"user_id": user_id},
            {"$set": {"chat_id": json.dumps(current_list)}},
            upsert=True,
        )
        return True

    def kureng_spgc(self, user_id, chat_id):
        spam_gc = self._db.spam_gc

        current_list = self.ambil_spgc(user_id)
        current_list.remove(chat_id)

        spam_gc.update_one(
            {"user_id": user_id}, {"$set": {"chat_id": json.dumps(current_list)}}
        )
        return True

    def ambil_spdb(self, user_id):
        spam_db = self._db.spam_db

        result = spam_db.find_one({"user_id": user_id}, {"_id": 0, "chat_id": 1})

        return json.loads(result["chat_id"]) if result and "chat_id" in result else []

    def tambah_spdb(self, user_id, chat_id):
        spam_db = self._db.spam_db

        current_list = self.ambil_spdb(user_id)
        current_list.append(chat_id)

        spam_db.update_one(
            {"user_id": user_id},
            {"$set": {"chat_id": json.dumps(current_list)}},
            upsert=True,
        )
        return True

    def kureng_spdb(self, user_id, chat_id):
        spam_db = self._db.spam_db

        current_list = self.ambil_spdb(user_id)
        current_list.remove(chat_id)

        spam_db.update_one(
            {"user_id": user_id}, {"$set": {"chat_id": json.dumps(current_list)}}
        )
        return True

monggo_uri = MONGO_URL
monggo = MongoDB(db_name="izzy", mongo_url=monggo_uri)

from PyroUbot.core.database.expired import *
from PyroUbot.core.database.get_uptime import *
from PyroUbot.core.database.notes import *
from PyroUbot.core.database.prefix import *
from PyroUbot.core.database.premium import *
from PyroUbot.core.database.reseller import *
from PyroUbot.core.database.saved import *
from PyroUbot.core.database.two_factor import *
from PyroUbot.core.database.userbot import *
from PyroUbot.core.database.variabel import *
