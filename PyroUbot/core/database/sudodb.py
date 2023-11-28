from PyroUbot.core.database import mongodb

sudodb = mongodb.sudo


async def get_sudo(user_id):
    seles = await sudodb.find_one({"sudo": "sudo"})
    if not seles:
        return []
    return seles["sudoer"]


async def add_sudo(user_id):
    sudoer = await get_sudo(user_id)
    sudoer.append(user_id)
    await sudodb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoer": sudoer}}, upsert=True
    )
    return True


async def remove_sudo(user_id):
    sudoer = await get_sudo(user_id)
    sudoer.remove(user_id)
    await sudodb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoer": sudoer}}, upsert=True
    )
    return True