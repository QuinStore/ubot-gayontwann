from PyroUbot.core.database import mongo_client

aktif = mongo_client["PyroUbot"]["cek_masa_aktif"]


async def get_uptime(user_id):
    user = await aktif.users.find_one({"_id": user_id})
    if user:
        return user.get("prefix")
    else:
        return None


async def set_uptime(user_id, expire_date):
    await aktif.users.update_one(
        {"_id": user_id}, {"$set": {"prefix": expire_date}}, upsert=True
    )


async def rem_uptime(user_id):
    await aktif.users.update_one(
        {"_id": user_id}, {"$unset": {"prefix": ""}}, upsert=True
    )
