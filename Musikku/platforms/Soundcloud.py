#
# Copyright (C) 2021-2022 by milokun@Github, < https://github.com/milokun >.
#
# This file is part of < https://github.com/milokun/Milomusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/milokun/Milomusic/blob/master/LICENSE >
#
# All rights reserved.

import re
from os import path

from yt_dlp import YoutubeDL

from Musikku.utils.formatters import seconds_to_min


class SoundAPI:
    def __init__(self):
        self.regex = r"^(https:\/\/soundcloud.com\/)(.*)$"
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "format": "best",
            "retries": 3,
            "nooverwrites": False,
            "continuedl": True,
        }

    async def valid(self, link: str):
        if re.search(self.regex, link):
            return True
        else:
            return False

    async def download(self, url):
        d = YoutubeDL(self.opts)
        try:
            info = d.extract_info(url)
        except:
            return False
        xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
        duration_min = seconds_to_min(info["duration"])
        track_details = {
            "title": info["title"],
            "duration_sec": info["duration"],
            "duration_min": duration_min,
            "uploader": info["uploader"],
            "filepath": xyz,
        }
        return track_details, xyz
