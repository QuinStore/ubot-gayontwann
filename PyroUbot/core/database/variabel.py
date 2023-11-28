from PyroUbot.core.database import mongodb

varsdb = mongodb.vars


async def set_vars(bot_id, vars_name, value):
    update_data = {"$set": {f"vars.{vars_name}": value}}
    await varsdb.update_one({"_id": bot_id}, update_data, upsert=True)


async def get_vars(bot_id, vars_name):
    result = await varsdb.find_one({"_id": bot_id})
    return result.get("vars").get(vars_name) if result else None


async def remove_all_vars(bot_id):
    await varsdb.delete_one({"_id": bot_id})
