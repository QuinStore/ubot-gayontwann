import asyncio

from pyrogram import filters
from pyrogram.types import Message

from PyroUbot import *
from PyroUbot.core.helpers.basic import edit_or_reply, extract_user, ReplyCheck


@ubot.on_message(filters.command("curhat") & filters.me)
async def ngecurhat(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "NI GW KASIH TAU..")
    await asyncio.sleep(1.5)
    await xx.edit("LU KALAU MAU CURHAT")
    await asyncio.sleep(1.5)
    await xx.edit("JANGAN KE GW LAH GBLK")
    await asyncio.sleep(1.5)
    await xx.edit("MALAS DENGAR CERITA LU KNTL")
    await asyncio.sleep(1.5)
    await xx.edit("CERITA KAGAK JELAS GBLK")
    await asyncio.sleep(1.5)
    await xx.edit("CURHAT YANG HASILIN DUIT KEK")
    await asyncio.sleep(1.5)
    await xx.edit("INI MALAH CURHAT SOAL KEHIDUPAN LU YG KEK TAII ANYING ITU")
    await asyncio.sleep(1.5)
    await xx.edit("LU CUMA CERITA SOAL KEPALSUAN HIDUP LU DOANG THOLOL")
    await asyncio.sleep(1.5)
    await xx.edit("NAMA JUGA BOCAHH PUBER")
    await asyncio.sleep(1.5)
    await xx.edit("DI SAKITINN ORANG TUA SEDIKIT NGAMBEK GBLK")
    await asyncio.sleep(1.5)
    await xx.edit("BANTU NOH ORANG TUA LU KASIHAN NGASIH LU MAKAN")


@ubot.on_message(filters.command("knl") & filters.me)
async def toxicknl(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "**Jangan replay**")
    await asyncio.sleep(1.5)
    await xx.edit("kita ga kenal")
    await asyncio.sleep(1.5)
    await xx.edit("kalau mau replay, replay aja sendiri")
    await asyncio.sleep(1.5)
    await xx.edit("ke akun lu, jangan reply ke gw")
    await asyncio.sleep(1.5)
    await xx.edit("ga keren lu begitu sok kenal")
    await asyncio.sleep(1.5)
    await xx.edit("lu kalau mau kenalan dipc aja:v")
    await asyncio.sleep(1.5)
    await xx.edit("jangan direplay, yang direplay aja banyak")
    await asyncio.sleep(1.5)
    await xx.edit("BHAHAHAHA")
    await asyncio.sleep(1.5)
    await xx.edit("apa lagi yang dichat kwkwkw bercanda")
    

@ubot.on_message(filters.command("umm") & filters.me)
async def toxicumm(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "umm boleh kenalan ga?")
    await asyncio.sleep(1.5)
    await xx.edit("anu kalau ga boleh gpp kok")
    await asyncio.sleep(1.5)
    await xx.edit("Tapi boong:v")
    await asyncio.sleep(1.5)
    await xx.edit("siapa juga yang mau kenal sama orang murahan")
    await asyncio.sleep(1.5)
    await xx.edit("sana sini mau, BAHAHAHA")
    await asyncio.sleep(1.5)
    await xx.edit("didekatin dikit langsung terima")
    await asyncio.sleep(1.5)
    await xx.edit("dibilang gatel si engga hehe")
    await asyncio.sleep(1.5)
    await xx.edit("TAPI DIBILANG MURAH IYA KWKWK")
    await asyncio.sleep(1.5)
    await xx.edit("UDAH MURAH MURAHAN LAGI GBLK BHAHA")

@ubot.on_message(filters.command("malu") & filters.me)
async def toxicmalu(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "eh gw mau nanya nih")
    await asyncio.sleep(1.5)
    await xx.edit("kau punya malu kan?")
    await asyncio.sleep(1.5)
    await xx.edit("kalau punya malu kok sikap nya kaya...")
    await asyncio.sleep(1.5)
    await xx.edit("ga punya malu?")
    await asyncio.sleep(1.5)
    await xx.edit("apa jangan jangan....")
    await asyncio.sleep(1.5)
    await xx.edit("urat malu kau putus?")
    await asyncio.sleep(1.5)
    await xx.edit("BHAHAHAHAHA KAGAK PUNYA MALU")
    await asyncio.sleep(1.5)
    await xx.edit("upp bercanda eh")
    await asyncio.sleep(1.5)
    await xx.edit("tapi seriusan emg lu punya urat malu???")

@ubot.on_message(filters.command("be") & filters.me)
async def toxicbe(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "OII BABIII")
    await asyncio.sleep(1.5)
    await xx.edit("OHH GA MAU DIPANGGIL BABII?")
    await asyncio.sleep(1.5)
    await xx.edit("tapi kok sikap nya kaya babii")
    await asyncio.sleep(1.5)
    await xx.edit("OHH IYA, LUPA KAN EMG ANAKK BABII")
    await asyncio.sleep(1.5)
    await xx.edit("KASIHAN ANAK BABII KWKWKWK")
    await asyncio.sleep(1.5)
    await xx.edit("MAKA NYA KALAU ENGGA MAU DI BILANG BEGINI")
    await asyncio.sleep(1.5)
    await xx.edit("SIKAP NYA JANGAN KAYA BABII GBLKK!")
    await asyncio.sleep(1.5)
    await xx.edit("BHAHAHAHA")
    await asyncio.sleep(1.5)
    await xx.edit("BERCANDA BABII")

@ubot.on_message(filters.command("psn") & filters.me)
async def toxicpsn(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "OII ANAK ANYINGG")
    await asyncio.sleep(1.5)
    await xx.edit("LUU KALAU MAU GCASTT")
    await asyncio.sleep(1.5)
    await xx.edit("JANGAN SPAM LAH GBLK!")
    await asyncio.sleep(1.5)
    await xx.edit("KAYA GC INI PUNYA NENEKK BAPACK LU")
    await asyncio.sleep(1.5)
    await xx.edit("SADARRR DIRII DEKKKK DEKKK")
    await asyncio.sleep(1.5)
    await xx.edit("PESAN SAMPAHH MALAH DIGCAST")
    await asyncio.sleep(1.5)
    await xx.edit("BARU BUAT BOTT APA GMN LUU")
    await asyncio.sleep(1.5)
    await xx.edit("NORAK!!")
    await asyncio.sleep(1.5)
    await xx.edit("GCAST BOLEH TAPI PAKE OTAK!")

@ubot.on_message(filters.command("kasihan") & filters.me)
async def toxickasihan(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "**OOOO**")
    await asyncio.sleep(1.5)
    await xx.edit("**INI NI YG HOBI NYA**")
    await asyncio.sleep(1.5)
    await xx.edit("**DEKAT SANA SINI**")
    await asyncio.sleep(1.5)
    await xx.edit("**MAU NGILANGIN KESEPIAN?**")
    await asyncio.sleep(1.5)
    await xx.edit("**NI INGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**LU KALAU KESEPIAN DOANGGGG**")
    await asyncio.sleep(1.5)
    await xx.edit("**MENDING JANGAN DEKAT SANA SINI GBLK**")
    await asyncio.sleep(1.5)
    await xx.edit("**KALAU LU KESEPIAN MENDING LU NGELONTEE SANA**")
    await asyncio.sleep(1.5)
    await xx.edit("**JANGAN BAWA BAWA ORANG LAIN KE DALAM MASALAH KESIAPAN LU GBLK!!**")


@ubot.on_message(filters.command("rosting") & filters.me)
async def toxicrosting(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "OI PPKK")
    await asyncio.sleep(1.5)
    await xx.edit("GA KEREN LU BEGITU")
    await asyncio.sleep(1.5)
    await xx.edit("NGATA NGATAIN ORANG ELIT")
    await asyncio.sleep(1.5)
    await xx.edit("PAS DIKATAIN SAMA ORANG SULIT")
    await asyncio.sleep(1.5)
    await xx.edit("PAS DI KATAIN DIAM KEK ORANG THOLOL MINTA AMPUN")
    await asyncio.sleep(1.5)
    await xx.edit("MAKA NYA JANGAN NGATAIN ORANG")
    await asyncio.sleep(1.5)
    await xx.edit("DIKATAIN BALIK GA TERIMA")
    await asyncio.sleep(1.5)
    await xx.edit("BHAHAHAHA")
    await asyncio.sleep(1.5)
    await xx.edit("BOCAHH BOCAHHH BHAHA")
    

@ubot.on_message(filters.command("peka") & filters.me)
async def toxicpeka(ubot: ubot, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "hi kak")
    await asyncio.sleep(1.5)
    await xx.edit("cuma mau bilang")
    await asyncio.sleep(1.5)
    await xx.edit("jadi orang tuh yang peka")
    await asyncio.sleep(1.5)
    await xx.edit("ditanya lagi apa malah jawab nya iya")
    await asyncio.sleep(1.5)
    await xx.edit("SOK JUAL MAHAL LU GBLK")
    await asyncio.sleep(1.5)
    await xx.edit("PAP TT LU TUH NOH NYANGKUT DIHP MANTAN LU")
    await asyncio.sleep(1.5)
    await xx.edit("SADAR DIRI GBLK, DI SERIUSIN SAMA ORANG YG SUKA SAMA LU")
    await asyncio.sleep(1.5)
    await xx.edit("MALAH DI CUEKIN, DAPAT YANG GANTENG CUMA MAU TUBUH LU MALAH DITERIMA, MANA CUMA DI PAKE LAGI")
    await asyncio.sleep(1.5)
    await xx.edit("MAKA NYA JADI ORANG TUHH YG PEKA DIKIT THOLOL JANGAN LANGSUNG DITERIMA")


__MODULE__ = "ᴛᴏxɪᴄ 1"
__HELP__ = f"""
<b>『 Toxic 』</b>

1. `malu` 
2. `curhat`
3. `umm`
4. `knl`
5. `be`
5. `psn`
7. `kasihan`
8. `rosting`
9. `peka`
"""


