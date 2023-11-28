from PyroUbot.core.database import mongo_client

collection = mongo_client["PyroUbot"]["notes"]


async def save_note(user_id, note_name, message):
    doc = {"_id": user_id, "notes": {note_name: message}}
    result = await collection.find_one({"_id": user_id})
    if result:
        await collection.update_one(
            {"_id": user_id}, {"$set": {f"notes.{note_name}": message}}
        )
    else:
        await collection.insert_one(doc)


async def get_note(user_id, note_name):
    result = await collection.find_one({"_id": user_id})
    if result is not None:
        try:
            note_id = result["notes"][note_name]
            return note_id
        except KeyError:
            return None
    else:
        return None


async def rm_note(user_id, note_name):
    await collection.update_one(
        {"_id": user_id}, {"$unset": {f"notes.{note_name}": ""}}
    )


async def all_notes(user_id):
    results = await collection.find_one({"_id": user_id})
    try:
        notes_dic = results["notes"]
        key_list = notes_dic.keys()
        return key_list
    except:
        return None


async def rm_all(user_id):
    await collection.update_one({"_id": user_id}, {"$unset": {"notes": ""}})
