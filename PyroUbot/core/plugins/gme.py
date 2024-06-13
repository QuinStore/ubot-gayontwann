import random
from PyroUbot.core.function.emoji import emoji

async def catur_cmd(client, message):
    try:
        x = await client.get_inline_bot_results("GameFactoryBot")
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[0].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)




async def game_cmd(client, message):
    try:
        x = await client.get_inline_bot_results("gamee")
        msg = message.reply_to_message or message
        random_index = random.randint(0, len(x.results) - 1)
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[random_index].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)