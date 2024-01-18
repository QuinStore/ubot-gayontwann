from PyroUbot.core.database import mongo_client

gcast_process = mongo_client["PyroUbot"]["proses"]


async def get_gcast_process(user_id):
    user = await gcast_process.users.find_one({"_id": user_id})
    if user:
        return user.get("gcast_process")
    else:
        return None


async def set_gcast_process(user_id, gcast_proces):
    await gcast_process.users.update_one(
        {"_id": user_id}, {"$set": {"gcast_process": gcast_proces}}, upsert=True
    )


async def rem_gcast_process(user_id):
    await gcast_process.users.update_one(
        {"_id": user_id}, {"$unset": {"gcast_process": ""}}, upsert=True
    )

gcast_sukses = mongo_client["PyroUbot"]["sukses"]

async def get_gcast_sukses(user_id):
    user = await gcast_sukses.users.find_one({"_id": user_id})
    if user:
        return user.get("gcast_sukses")
    else:
        return None


async def set_gcast_sukses(user_id, gcast_suksess):
    await gcast_sukses.users.update_one(
        {"_id": user_id}, {"$set": {"gcast_sukses": gcast_suksess}}, upsert=True
    )


async def rem_gcast_sukses(user_id):
    await gcast_sukses.users.update_one(
        {"_id": user_id}, {"$unset": {"gcast_sukses": ""}}, upsert=True
    )

ping_pong = mongo_client["PyroUbot"]["pong"]

async def get_ping_pong(user_id):
    user = await ping_pong.users.find_one({"_id": user_id})
    if user:
        return user.get("ping_pongs")
    else:
        return None


async def set_ping_pong(user_id, ping_pongs):
    await ping_pong.users.update_one(
        {"_id": user_id}, {"$set": {"ping_pongs": ping_pongs}}, upsert=True
    )


async def rem_ping_pong(user_id):
    await ping_pong.users.update_one(
        {"_id": user_id}, {"$unset": {"ping_pongs": ""}}, upsert=True
    )

ping_uptime = mongo_client["PyroUbot"]["uptime"]

async def get_ping_uptime(user_id):
    user = await ping_uptime.users.find_one({"_id": user_id})
    if user:
        return user.get("ping_uptimes")
    else:
        return None


async def set_ping_uptime(user_id, ping_uptimes):
    await ping_uptime.users.update_one(
        {"_id": user_id}, {"$set": {"ping_uptimes": ping_uptimes}}, upsert=True
    )


async def rem_ping_uptime(user_id):
    await ping_uptime.users.update_one(
        {"_id": user_id}, {"$unset": {"ping_uptimes": ""}}, upsert=True
    )

ping_mention = mongo_client["PyroUbot"]["mention"]

async def get_ping_mention(user_id):
    user = await ping_mention.users.find_one({"_id": user_id})
    if user:
        return user.get("ping_mentions")
    else:
        return None


async def set_ping_mention(user_id, ping_mentions):
    await ping_mention.users.update_one(
        {"_id": user_id}, {"$set": {"ping_mentions": ping_mentions}}, upsert=True
    )


async def rem_ping_mention(user_id):
    await ping_mention.users.update_one(
        {"_id": user_id}, {"$unset": {"ping_mentions": ""}}, upsert=True
    )


