async def izzy_meira(client):
    group_name = "Juan Botlog"
    async for dialog in client.get_dialogs():
        if dialog.chat.title == group_name:
            return dialog.chat
    return None

async def meira(client):
    group_name = "Juan Botlog"
    group_description = "Juan Botlog Group"
    group = await izzy_meira(client)
    if group is None:
        await client.create_supergroup(group_name, group_description)
        #await client.send_message(group.id, group_message)
        group = await izzy_meira(client)  # Fetch the created group
    return None