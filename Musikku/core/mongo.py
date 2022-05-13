#
# Copyright (C) 2021-2022 by milokun@Github, < https://github.com/milokun >.
#
# This file is part of < https://github.com/milokun/Milomusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/milokun/Milomusic/blob/master/LICENSE >
#
# All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient

import config

_mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
_mongo_sync_ = MongoClient(config.MONGO_DB_URI)

mongodb = _mongo_async_.Milomusic
pymongodb = _mongo_sync_.Milomusic
