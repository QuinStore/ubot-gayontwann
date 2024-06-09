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

__MODULE__ = "download"
__HELP__ = """
 <b>Bantuan Untuk Download</b>

• <b>Perintah</b> : <code>{0}tt</code> <b>[link nya]</b>
• <b>Penjelasan : Download Vt No Vm</b>

• <b>Perintah</b> : <code>{0}ig</code> <b>[link nya]</b>
• <b>Penjelasan : Download Vidio Instagram</b>

• <b>Perintah</b> : <code>{0}pint</code> <b>[link nya]</b>
• <b>Penjelasan : Download Foto Pinterest</b>

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

class PinterestMediaDownloader:
	info_url = "https://api.pinterest.com/v3/pidgets/pins/info/?pin_ids={}"
	
	def __init__(self, pin_url):
		self.session = requests.Session()
		self.pin_url = pin_url
		self.pin_id = None
		self.media = []
		self.data = None
		self.best_sizes = []

	def get_pin_id(self):
		history = self.session.get(self.pin_url).history
		self.pin_id = history[-1].headers["location"].split("/")[4] if history else self.pin_url.split("/")[4]

	def get_pin_data(self):
		self.data = self.session.get(self.__class__.info_url.format(self.pin_id)).json()["data"][0]
	  
	def get_pin_media(self): 
		if spd := self.data.get("story_pin_data"):
			for page in spd["pages"]:
				if v := page["blocks"][0].get("video"):
					self.media.append(v.get("video_list")) 

				elif i := page["blocks"][0].get("image"):
					self.media.append(i.get("images"))
				else:
					pass
		elif v := self.data.get("videos"):
			self.media.append(v.get("video_list"))
		elif i := self.data.get("images"):
			self.media.append(i)
		else:
			pass
		
	def get_best_sizes(self):
		for i, m in enumerate(self.media):
			for s in list(m):
				if m[s]["url"].strip().endswith(".m3u8"):
					m.pop(s)
			new_m = sorted(m.values(), key=lambda s: s["width"]*s["height"], reverse=True)
			
			self.best_sizes.append(new_m[0])


#pinterest downloader
@PY.UBOT("pint")
async def pinterest(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Untuk mendapatkan media Pinterest lakukan /pints [URL Pinterest]")

    content = message.text.split(None, 1)[1]
    pinterest_downloader = PinterestMediaDownloader(content)
    
    i = await message.reply_text("🔍 <b>Memprosess...</b>")
    
    try:
        pinterest_downloader.get_pin_id()
        pinterest_downloader.get_pin_data()
        pinterest_downloader.get_pin_media()
        pinterest_downloader.get_best_sizes()

        best_media_url = pinterest_downloader.best_sizes[0]["url"]
        file_extension = best_media_url.split('.')[-1]
        caption = f"• Powered by WannFyy\n\nFile type: {file_extension.capitalize()}"
        
        if any('.mp4' in best_media_url for media in pinterest_downloader.best_sizes):
            await message.reply_video(best_media_url, caption=caption)
        elif any('.gif' in best_media_url for media in pinterest_downloader.best_sizes):
            await message.reply_animation(best_media_url, caption=caption)
        else:
            await message.reply_photo(best_media_url, caption=caption)
        
        await i.delete()
    except Exception as err:
        return await i.edit("Maaf, saya tidak dapat mendapatkan informasi tentang file ini.\nCoba lagi nanti atau kirim tautan lain.", disable_web_page_preview=True)


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


#ig downloader    
PY.UBOT("ig")
async def link_handler(client, message):
    if len(message.text.split()) < 2:
        await message.reply_text("/ig [berikan url yang benar]")
        return

    link = message.text.split()[1]
    try:
        m = await message.reply_text("⏳")
        url= link.replace("instagram.com","ddinstagram.com")
        url=url.replace("==","%3D%3D")
        if url.endswith("="):
           dump_file=await message.reply_video(url[:-1])
        else:
            dump_file=await message.reply_video(url)
        await m.delete()
    except Exception as e:
        try:
            if "/reel/" in url or "/p/" in url:
               getdata = requests.get(url).text
               soup = bs4.BeautifulSoup(getdata, 'html.parser')
               meta_tags = soup.find_all('meta', attrs={'property': 'og:video'})
               if not meta_tags:
                  meta_tags = soup.find_all('meta', attrs={'property': 'og:image'})    
               for meta_tag in meta_tags:
                   content_value = meta_tag['content']
                   try:
                       dump_file=await message.reply_video(f"https://ddinstagram.com{content_value}")
                   except:
                       downfile=wget.download(f"https://ddinstagram.com{content_value}")
                       dump_file=await message.reply_video(downfile) 
        except Exception as e:
            await message.reply_text(f"https://ddinstagram.com{content_value}")
            tracemsg=traceback.extract_tb(e.__traceback__)
            await message.reply(tracemsg)
            await message.reply(f"400: Sorry, Unable To Find It  try another or report it  to @vckys or support chat @geezram 🤖  ")

        finally:
            await m.delete()
            if 'downfile' in locals():
                os.remove(downfile)
