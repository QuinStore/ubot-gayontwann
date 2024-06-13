import os
import bs4
import wget
import requests
import traceback
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "Instagram"
__HELP__ = """
 <b>Bantuan Untuk Instagram</b>

• <b>Perintah</b> : <code>{0}insta</code> <b>[link]</b>
• <b>Penjelasan : Downloader Vid Insta</b>

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

@PY.UBOT("insta")
async def instacrot(client: Client, message):
    print("processing")
    if len(message.text.split()) < 2:
        await message.reply_text("/ig [berikan url yang benar]")
        return

    link = message.text.split()[1]
    try:
        m = await message.reply_text("⏳")
        url = link.replace("instagram.com", "ddinstagram.com")
        url = url.replace("==", "%3D%3D")
        if url.endswith("="):
            dump_file = await message.reply_video(url[:-1])
        else:
            dump_file = await message.reply_video(url)
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
                        dump_file = await message.reply_video(f"https://ddinstagram.com{content_value}")
                    except:
                        downfile = wget.download(f"https://ddinstagram.com{content_value}")
                        dump_file = await message.reply_video(downfile)
        except Exception as e:
            await message.reply_text(f"https://ddinstagram.com{content_value}")
            tracemsg = traceback.format_exc()
            await message.reply_text(tracemsg)
            await message.reply_text("400: Sorry, Unable To Find It  try another or report it  to @vckys or support chat @geezram 🤖")
        finally:
            await m.delete()
            if 'downfile' in locals():
                os.remove(downfile)
