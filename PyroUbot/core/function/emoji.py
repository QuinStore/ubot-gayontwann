def emoji(alias):
    emojis = {
        "bintang": "<emoji id=5911461474315802019>⭐</emoji>",
        "loading": "<emoji id=5801044672658805468>✨</emoji>",
        "proses": "<emoji id=6276248783525251352>🔄</emoji>",
        "gagal": "<emoji id=6278161560095426411>❌</emoji>",
        "done": "<emoji id=6278555627639801385>✅</emoji>",
        "upload": "<emoji id=5911100572508885928>♻️</emoji>",
    }
    return emojis.get(alias, "ᴇᴍᴏᴊɪ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.")
