from PyroUbot.core.database import mongo_client

sudo_db = mongo_client["PyroUbot"]["sudoers"]


async def get_sudos(user_id):
    sudoers_data = await sudo_db.find_one({"_id": str(user_id)})
    if not sudoers_data:
        return []
    return sudoers_data.get("sudoers", [])

async def add_sudos(user_id, sudo_user_id):
    sudoers = await get_sudos(user_id)
    if sudo_user_id not in sudoers:
        sudoers.append(sudo_user_id)
        await sudo_db.update_one(
            {"_id": str(user_id)},
            {"$set": {"sudoers": sudoers}},
            upsert=True
        )
        return True
    return False

async def remove_sudos(user_id, sudo_user_id):
    sudoers = await get_sudos(user_id)
    if sudo_user_id in sudoers:
        sudoers.remove(sudo_user_id)
        await sudo_db.update_one(
            {"_id": str(user_id)},
            {"$set": {"sudoers": sudoers}},
            upsert=True
        )
        return True
    return False