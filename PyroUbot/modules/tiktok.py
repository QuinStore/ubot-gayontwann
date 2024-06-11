import re
import os
import bs4
import sys
import time
import math
import wget
import random
import base64
import requests
import traceback
from base64 import b64decode
from PyroUbot import *

__MODULE__ = "Tiktok"
__HELP__ = """
 <b>Bantuan Untuk Tiktok</b>

• <b>Perintah</b> : <code>{0}tt</code> <b>[link nya]</b>
• <b>Penjelasan : Download Vt No Vm</b>

"""

class TikTokDownloaderAPI:
    def __init__(self):
        pass
    def ttscraper(self, url, output_name):
        ses = requests.Session()
        i = ses.post('https://ytpp3.com/ttscraper/parse', data={'url': url})
        if '"message":"success"' in i.text:
            load = i.json()
            url_download = load['data']['nwm_video_url']
            get_content = requests.get(url_download)
            with open(output_name, 'wb') as fd:
                fd.write(get_content.content)
            return True
        else:
            return False

    def downloader(self, url, output_name):
        '''
        url: tiktok video url
        output_name: output video (.mp4). Example : video.mp4
        '''
        ses = requests.Session()
        server_url = 'https://musicaldown.com/'
        headers = {
            'Host': 'musicaldown.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers'
        }
        ses.headers.update(headers)
        req = ses.get(server_url)
        data = {}
        parse = bs4.BeautifulSoup(req.text, 'html.parser')
        get_all_input = parse.findAll('input')

        for i in get_all_input:
            if i.get("id") == 'link_url':
                data[i.get('name')] = url
            else:
                data[i.get('name')] = i.get('value')

        post_url = server_url + "id/download"
        req_post = ses.post(post_url, data=data, allow_redirects=True)
        if req_post.status_code == 302 or 'This video is currently not available' in req_post.text or 'Video is private or removed!' in req_post.text:
            print('- video private or remove')
            return 'private/remove'
        elif 'Submitted Url is Invalid, Try Again' in req_post.text:
            print('- url is invalid')
            return 'url-invalid'
        get_all_blank = bs4.BeautifulSoup(req_post.text, 'html.parser').findAll(
            'a', attrs={'target': '_blank'})

        download_link = get_all_blank[0].get('href')
        get_content = requests.get(download_link)

        with open(output_name, 'wb') as fd:
            fd.write(get_content.content)
        return True

#tiktok downloader
@PY.UBOT("tt")
async def tiktok(client, message):
    if len(message.command) < 2:
        text = (
            'Anda harus mengirimkan url yang benar untuk mendapatkan video dari TikTok.\n'
            'Contoh:\n'
            '- https://vt.tiktok.com/ZSN5V7BFX/\n'
        )
        return await message.reply_text(text, disable_web_page_preview=True)

    val = TikTokDownloaderAPI()
    value = message.text.split(None, 1)[1]

    if 'tiktok.com' in value and 'https://' in value:
        message_wait = await message.reply_text("🔍 <b>Memprosess...</b>")

        video = val.downloader(url=value, output_name='video.mp4')
        video_id = open('video.mp4', 'rb')

        if video:         
            await client.send_video(message.chat.id, video_id, caption="• Powered by WannFyy")  
        else:
            await message_wait.edit("Maaf, saya tidak dapat mendapatkan informasi tentang file ini.\nCoba lagi nanti atau kirim tautan lain.")

        await message_wait.delete()  
    else:
        text = (
            'Anda mengirimkan tautan yang salah ke postingan, silakan kirim tautan yang benar.\n'
            'Contoh:\n'
            '- https://vt.tiktok.com/ZSN5V7BFX/\n'
        )
        return await client.send_message(message.chat.id, text, disable_web_page_preview=True)

    await message.delete()
