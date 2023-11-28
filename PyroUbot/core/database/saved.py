from PyroUbot.core.database import mongodb

chatsdb = mongodb.chats


async def get_chat(user_id):
    chat = await chatsdb.find_one({"chat": user_id})
    if not chat:
        return []
    return chat["list"]


async def add_chat(user_id, chat_id):
    list = await get_chat(user_id)
    list.append(chat_id)
    await chatsdb.update_one({"chat": user_id}, {"$set": {"list": list}}, upsert=True)
    return True


async def remove_chat(user_id, chat_id):
    list = await get_chat(user_id)
    list.remove(chat_id)
    await chatsdb.update_one({"chat": user_id}, {"$set": {"list": list}}, upsert=True)
    return True
