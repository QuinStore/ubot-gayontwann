
from PyroUbot.core.database import mongo_client

afkdb = mongo_client["pyro_ubot"]["afk"]

async def go_afk(user_id: int, time, reason=""):
    user_data = await afkdb.users.find_one({"user_id": user_id})
    if user_data:
        await afkdb.users.update_one(
            {"user_id": user_id},
            {"$set": {"afk": True, "time": time, "reason": reason}},
        )
    else:
        await afkdb.users.insert_one(
            {"user_id": user_id, "afk": True, "time": time, "reason": reason}
        )


async def no_afk(user_id: int):
    await afkdb.users.delete_one({"user_id": user_id, "afk": True})


async def check_afk(user_id: int):
    user_data = await afkdb.users.find_one({"user_id": user_id, "afk": True})
    return user_data