from asyncio import get_event_loop
from functools import partial

from yt_dlp import YoutubeDL


def run_sync(func, *args, **kwargs):
    return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))


async def YoutubeDownload(url, as_video=False):
    if as_video:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    else:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    data_ytp = "<b>💡 ɪɴꜰᴏʀᴍᴀsɪ {}</b>\n\n<b>🏷 ɴᴀᴍᴀ:</ʙ> {}<b>\n<b>🧭 ᴅᴜʀᴀsɪ:</b> {}\n<b>👀 ᴅɪʟɪʜᴀᴛ:</b> {}\n<b>📢 ᴄʜᴀɴɴᴇʟ:</b> {}\n<b>🔗 ᴛᴀᴜᴛᴀɴ:</b> <a href={}>ʏᴏᴜᴛᴜʙᴇ</a>\n\n<b>⚡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> {}"
    ydl = YoutubeDL(ydl_opts)
    ytdl_data = await run_sync(
        ydl.extract_info,
        url,
        download=True,
    )
    file_name = ydl.prepare_filename(ytdl_data)
    videoid = ytdl_data["id"]
    title = ytdl_data["title"]
    url = f"https://youtu.be/{videoid}"
    duration = ytdl_data["duration"]
    channel = ytdl_data["uploader"]
    views = f"{ytdl_data['view_count']:,}".replace(",", ".")
    thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    return file_name, title, url, duration, views, channel, thumb, data_ytp
