from asyncio import run

from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(name="pyrogram", api_id=API_ID, api_hash=API_HASH, in_memory=True)


async def main():
    await i.start()
    ss = await i.export_session_string()
    await i.send_message(
        i.me.id,
        f"""
STRING_PYROGRAM

`{ss}`

YOUR_ID: {i.me.id}
""",
    )
    print("Silahkan Cek Pesan Tersimpan Anda")


run(main())
