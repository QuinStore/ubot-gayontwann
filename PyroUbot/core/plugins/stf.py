async def staff_cmd(client, message):
    chat_title = message.chat.title
    creator = []
    co_founder = []
    admin = []
    async for x in message.chat.get_members():
        mention = f"<a href=tg://user?id={x.user.id}>{x.user.first_name} {x.user.last_name or ''}</a>"
        if (
            x.status.value == "administrator"
            and x.privileges
            and x.privileges.can_promote_members
        ):
            if x.custom_title:
                co_founder.append(f" ┣ {mention} - {x.custom_title}")
            else:
                co_founder.append(f" ┣ {mention}")
        elif x.status.value == "administrator":
            if x.custom_title:
                admin.append(f" ┣ {mention} - {x.custom_title}")
            else:
                admin.append(f" ┣ {mention}")
        elif x.status.value == "owner":
            if x.custom_title:
                creator.append(f" ┗ {mention} - {x.custom_title}")
            else:
                creator.append(f" ┗ {mention}")
    if not co_founder and not admin:
        result = f"""
<b>sᴛᴀꜰꜰ ɢʀᴜᴘ
{chat_title}

👑 ᴏᴡɴᴇʀ:
{creator[0]}</b>"""
    elif not co_founder:
        adm = admin[-1].replace("┣", "┗")
        admin.pop(-1)
        admin.append(adm)
        result = f"""
<b>sᴛᴀꜰꜰ ɢʀᴜᴘ
{chat_title}

👑 ᴏᴡɴᴇʀ:
{creator[0]}

👮 ᴀᴅᴍɪɴ:</b>
""" + "\n".join(
            admin
        )
    elif not admin:
        cof = co_founder[-1].replace(" ┣", " ┗")
        co_founder.pop(-1)
        co_founder.append(cof)
        result = f"""
<b>sᴛᴀꜰꜰ ɢʀᴜᴘ
{chat_title}

👑 ᴏᴡɴᴇʀ:
{creator[0]}

👮 ᴄᴏ-ꜰᴏᴜɴᴅᴇʀ:</b>
""" + "\n".join(
            co_founder
        )
    else:
        adm = admin[-1].replace(" ┣", " ┗")
        admin.pop(-1)
        admin.append(adm)
        cof = co_founder[-1].replace(" ┣", " ┗")
        co_founder.pop(-1)
        co_founder.append(cof)
        result = (
            (
                f"""
<b>sᴛᴀꜰꜰ ɢʀᴜᴘ
{chat_title}

👑 ᴏᴡɴᴇʀ:
{creator[0]}

👮 ᴄᴏ-ꜰᴏᴜɴᴅᴇʀ:</b>
"""
                + "\n".join(co_founder)
                + """

<b>👮 ᴀᴅᴍɪɴ:</b>
"""
            )
            + "\n".join(admin)
        )

    await message.reply(result)
