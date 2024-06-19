from PyroUbot.core.database import mongodb

logrupdb = mongodb.logger

async def get_log_group(user_id: int) -> bool:
    cek = await logrupdb.find_one({"user_id": user_id})
    if not cek:
        return None
    return cek["logger"]

async def get_botlog(user_id: int):
    user_data = await logrupdb.users.find_one({"user_id": user_id})
    botlog_chat_id = user_data.get("bot_log_group_id") if user_data else None
    return botlog_chat_id


async def set_botlog(user_id: int, botlog_chat_id: int):
    await logrupdb.users.update_one(
        {"user_id": user_id},
        {"$set": {"bot_log_group_id": botlog_chat_id}},
        upsert=True,
    )

async def set_log_group(user_id: int, logger):
    cek = await get_log_group(user_id)
    if cek:
        await logrupdb.update_one({"user_id": user_id}, {"$set": {"logger": logger}})
    else:
        await logrupdb.insert_one({"user_id": user_id, "logger": logger})


async def del_log_group(user_id: int):
    await logrupdb.delete_one({"user_id": user_id})


async def get_log_groups(user_id: int):
    user_data = await logrupdb.users.find_one({"user_id": user_id})
    botlog_chat_id = user_data.get("bot_log_group_id") if user_data else []
    return botlog_chat_id