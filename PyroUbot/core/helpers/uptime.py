from time import time as waktunya

start_time = waktunya()


async def get_time(seconds):
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "ᴍ", "ʜ", "ᴅ", "ᴡ", "ᴍᴏ"]

    while count < 6:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        elif count < 4:
            remainder, result = divmod(seconds, 24)
        elif count < 5:
            remainder, result = divmod(seconds, 7)
        else:
            remainder, result = divmod(seconds, 30 * 24 * 60 * 60)

        if seconds == 0 and remainder == 0:
            break

        time_list.append(int(result))
        seconds = int(remainder)

    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]

    if len(time_list) >= 4:
        up_time += time_list.pop() + ":"

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
