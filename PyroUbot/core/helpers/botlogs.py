import pyrogram

async def izzy_meira(client):
    group_name = "lancarjaya botlog"
    async for dialog in client.get_dialogs():
        if dialog.chat.title == group_name:
            return dialog.chat
    return None

async def meira(client):
    group_name = "lancarjaya botlog"
    group_description = "lancarjaya botlog Group"
    #group = await izzy_meira(client)
    if group is None:
        try:
            group = await client.create_supergroup(group_name, group_description)
        except pyrogram.errors.exceptions.not_acceptable_406.ChannelPrivate:
            print("Failed to create the group. Please check your bot's permissions and try again.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return group