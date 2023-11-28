import re
import urllib

from search_engine_parser import GoogleSearch

from PyroUbot import *

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


async def google_search(client, message):
    webevent = await message.reply("<code>ᴍᴇɴᴇʟᴜsᴜʀɪ ɢᴏᴏɢʟᴇ...</code>")
    match = get_arg(message)
    if not match:
        return await webevent.edit(f"<code>{message.text} ǫᴜᴇʀʏ</code>")
    page = re.findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except Exception:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"- <a href={link}>{title}</a>\n<b>{desc}</b>\n\n"
        except Exception:
            passe
    return await webevent.edit(
        "<b>ᴍᴇɴᴇʟᴜsᴜʀɪ  ǫᴜᴇʀʏ:</b>\n<code>"
        + match
        + "</code>\n\n<b>ʀᴇsᴜʟᴛs:</b>\n"
        + msg,
        disable_web_page_preview=True,
    )
