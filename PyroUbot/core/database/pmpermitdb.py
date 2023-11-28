from PyroUbot.core.database import mongodb

pmdb = mongodb.pmpermit

async def add_approved_user(user_id):
    good_usr = int(user_id)
    does_they_exists = await pmdb.find_one({"user_id": "APPROVED_USERS"})
    if does_they_exists:
        await pmdb.update_one(
            {"user_id": "APPROVED_USERS"}, {"$push": {"good_id": good_usr}}
        )
    else:
        await pmdb.insert_one({"user_id": "APPROVED_USERS", "good_id": [good_usr]})


async def rm_approved_user(user_id):
    bad_usr = int(user_id)
    does_good_ones_exists = await pmdb.find_one({"user_id": "APPROVED_USERS"})
    if does_good_ones_exists:
        await pmdb.update_one(
            {"user_id": "APPROVED_USERS"}, {"$pull": {"good_id": bad_usr}}
        )
    else:
        return None


async def check_user_approved(user_id):
    random_usr = int(user_id)
    does_good_users_exists = await pmdb.find_one({"user_id": "APPROVED_USERS"})
    if does_good_users_exists:
        good_users_list = [
            cool_user for cool_user in does_good_users_exists.get("good_id")
        ]
        if random_usr in good_users_list:
            return True
        else:
            return False
    else:
        return False