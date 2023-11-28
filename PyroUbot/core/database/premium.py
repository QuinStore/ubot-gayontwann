from PyroUbot.core.database import mongodb

user = mongodb.premium


async def get_prem():
    prem = await user.find_one({"prem": "prem"})
    if not prem:
        return []
    return prem["list"]


async def add_prem(user_id):
    list = await get_prem()
    list.append(user_id)
    await user.update_one({"prem": "prem"}, {"$set": {"list": list}}, upsert=True)
    return True


async def remove_prem(user_id):
    list = await get_prem()
    list.remove(user_id)
    await user.update_one({"prem": "prem"}, {"$set": {"list": list}}, upsert=True)
    return True
