#
# Copyright (C) 2021-2022 by milokun@Github, < https://github.com/milokun >.
#
# This file is part of < https://github.com/milokun/Milomusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/milokun/Milomusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from Musikku import app
from Musikku.core.call import Musikku
from Musikku.utils.database import is_muted, mute_on
from Musikku.utils.decorators import AdminRightsCheck

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(
    filters.command(MUTE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    await mute_on(chat_id)
    await Musikku.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention)
    )
