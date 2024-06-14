import asyncio
from pyrogram import filters
from pyrogram.types import Message
from PyroUbot import *
from PyroUbot.core.helpers.basic import edit_or_reply, extract_user, ReplyCheck

DEVS = [1344553362]

@ubot.on_message(filters.command("jamet") & filters.me)
async def ngejamet(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "WOII")
    await asyncio.sleep(1.5)
    await xx.edit("Lu yang rusuh sana sini?")
    await asyncio.sleep(1.5)
    await xx.edit("Ni gw bilang ya")
    await asyncio.sleep(1.5)
    await xx.edit("GAUSAH SO ASIK")
    await asyncio.sleep(1.5)
    await xx.edit("EMANG LU TERKENAL?")
    await asyncio.sleep(1.5)
    await xx.edit("Cuma kacung di real sok mau rusuh")
    await asyncio.sleep(1.5)
    await xx.edit("Orang yang kaya lu ni harus gw katain")
    await asyncio.sleep(1.5)
    await xx.edit("Jangan sok tinggi di telegram bgstt")
    await asyncio.sleep(1.5)
    await xx.edit("BOCAH KAMPUNG")
    await asyncio.sleep(1.5)
    await xx.edit("THOLOL KALAU LU MAU RUSUH JANGAN DISINI THOLOL")
    await asyncio.sleep(1.5)
    await xx.edit("Mending lu bantu mak lu sono, dari pada ga ada kerjaan")


@ubot.on_message(filters.command("bct") & filters.me)
async def bct(ubot: ubot, message: Message):
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "Apa luh ga senang?",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("poto") & filters.me)
async def poto(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "Yang ga punya pp, itu sangeann ya goblokk!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("ppx") & filters.me)
async def toxicppx(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "OI PPKK LU KALAU MAU NIMBRUNG, NIMBRUNG AJA GOBLOKKK JGN RUSUHH DISINII THOLOL!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("so") & filters.me)
async def toxicso(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "Ni gw bilang yah.., jangan sok kntll thololll lu siapaaa!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("nrk") & filters.me)
async def toxicnrk(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BLACKLIST_CHAT:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "MAEN BOT MULU ALAY NGENTOTT, KESANNYA NORAK GOBLOK!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("sni") & filters.me)
async def toxicsni(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("war") & filters.me)
async def toxicwer(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GBLKK MENDING LU KERJA SANA PENGANGGURAN LU BBII.",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("cpr") & filters.me)
async def toxiccpr(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("kis") & filters.me)
async def toxickis(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "CUIHHHH, NIH GW CIUM PALA OTAK KAU, KAU PUNYA OTAK GA GBLKK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("van") & filters.me)
async def toxicvan(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "Apa kau pantex, mau apa mau pc pc gw anying",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("sokab") & filters.me)
async def toxicsokab(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("gembel") & filters.me)
async def toxicgembel(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("cuih") & filters.me)
async def toxiccuih(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("dih") & filters.me)
async def toxicdih(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("gc") & filters.me)
async def toxicgc(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BLACKLIST_CHAT:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "INI GC APA SI ANYING SEPI BANGET KEK GC MATI, GC SAMPAH KAYA GINI, MENDING BUBARIN AJA GBLK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("hah") & filters.me)
async def toxichah(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        ubot.send_message(
            message.chat.id,
            "EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("vir") & filters.me)
async def toxicvir(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "**OOOO**")
    await asyncio.sleep(1.5)
    await xx.edit("**INI YANG VIRTUAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**YANG KATANYA SAYANG BANGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TAPI TETEP AJA DI TINGGAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**NI INGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**APALAGI KEMALUAN NYA**")
    await asyncio.sleep(1.5)
    await xx.edit("**BHAHAHAHA**")
    await asyncio.sleep(1.5)
    await xx.edit("**KASIAN BAHAHAHA GBLOK MKN TUH VIRTUAL**")




__MODULE__ = "ᴛᴏxɪᴄ 2"
__HELP__ = f"""
<b>『 Toxic 』</b>

<b>• Bct  | • jamet</b>
<b>• vir  | • cuih</b>
<b>• poto | • gembel</b>
<b>• so   | • sni</b>
<b>• hah  | • ppx</b>
<b>• nrk  | • war</b>
<b>• cpr  | • kis</b>
<b>• van  | • gcast</b>
<b>• sokab</b>
"""


