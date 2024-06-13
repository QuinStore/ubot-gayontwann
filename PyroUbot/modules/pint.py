import os
import bs4
import wget
import requests
import traceback
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "pinterest"
__HELP__ = """
 <b>Bantuan Untuk Pinterest</b>

• <b>Perintah</b> : <code>{0}pint</code> <b>[link nya]</b>
• <b>Penjelasan : Download Foto Pinterest</b>

"""

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
