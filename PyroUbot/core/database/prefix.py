from PyroUbot.core.database import mongo_client

prefixes = mongo_client["PyroUbot"]["prefixes"]


async def get_pref(user_id):
    user = await prefixes.users.find_one({"_id": user_id})
    if user:
        return user.get("prefix")
    else:
        return None


async def set_pref(user_id, prefix):
    await prefixes.users.update_one(
        {"_id": user_id}, {"$set": {"prefix": prefix}}, upsert=True
    )


async def rem_pref(user_id):
    await prefixes.users.update_one(
        {"_id": user_id}, {"$unset": {"prefix": ""}}, upsert=True
    )
