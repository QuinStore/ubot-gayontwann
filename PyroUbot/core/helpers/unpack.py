from base64 import urlsafe_b64decode
from struct import unpack

from attrify import Attrify as Atr


def unpackInlineMessage(inline_message_id: str):
    dc_id, message_id, chat_id, query_id = unpack(
        "<iiiq",
        urlsafe_b64decode(
            inline_message_id + "=" * (len(inline_message_id) % 4),
        ),
    )
    temp = {
        "dc_id": dc_id,
        "message_id": message_id,
        "chat_id": int(str(chat_id).replace("-1", "-1001")),
        "query_id": query_id,
        "inline_message_id": inline_message_id,
    }
    return Atr(temp)
