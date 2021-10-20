from __future__ import annotations

import requests as req
from datetime import datetime
from typing import Dict, List
import StandardLibrary.Utils.Configuration as Configuration


class Notion:
    baseURL = Configuration.notion_baseURL()
    version = 'v1'

    class Database:
        def create_database(databaseID: str, args, *kwargs) -> Dict:
            pass

        def update_database(databaseID: str, args, *kwargs) -> Dict:
            pass

        def retrieve_database(databaseID: str, args, *kwargs) -> Dict:
            pass

        def query(databaseID: str, args, *kwargsclea) -> Dict:
            pass

    class Page:
        def create_page(databaseID: str, args, *kwargs) -> Dict:
            pass

        def retrive_page(databaseID: str, args, *kwargs) -> Dict:
            pass

        def update_page(databaseID: str, args, *kwargs) -> Dict:
            pass

    class Block:
        pass

    def __init__(self, default_db: str, auth: str, version: str = 'v1') -> None:
        self.version = version
        self.default_db = default_db
        self.auth = auth
        self.version = version

        self.header = {
            "Authorization": "Bearer " + auth,
            "Content-Type": "application/json",
            "Notion-Version": datetime.now().strftime('%Y-%m-%d')
        }
