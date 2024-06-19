from userbot.core.database import mongodb

logrupdb = mongodb.logger

async def get_log_group(user_id: int) -> bool:
    cek = await logrupdb.find_one({"user_id": user_id})
    if not cek:
        return None
    return cek["logger"]


async def set_log_group(user_id: int, logger):
    cek = await get_log_group(user_id)
    if cek:
        await logrupdb.update_one({"user_id": user_id}, {"$set": {"logger": logger}})
    else:
        await logrupdb.insert_one({"user_id": user_id, "logger": logger})


async def del_log_group(user_id: int):
    await logrupdb.delete_one({"user_id": user_id})
