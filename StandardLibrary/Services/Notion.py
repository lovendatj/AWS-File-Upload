from __future__ import annotations

import requests as req
from datetime import datetime
from typing import Tuple
import StandardLibrary.Utils.Configuration as Configuration
from StandardLibrary.Utils.FileData import jsonify, write_json


class Notion:
    baseURL = Configuration.notion_baseURL()
    version = 'v1'

    def __init__(self, auth: str, defaultDB: str = None, version: str = 'v1') -> None:
        self.version = version
        self.default_db = defaultDB
        self.auth = auth
        self.version = version

        self.header = {
            "Authorization": f"Bearer {auth}",
            "Content-Type": "application/json",
            "Notion-Version": "2021-08-16"
        }

    def post(self, url: str, data: dict) -> dict:
        url = f'{Notion.baseURL}/{Notion.version}/{url}/'
        print(f'[POST] {url}')
        return req.post(url, headers=self.header, data=data)

    def get(self, url: str) -> dict:
        url = f'{Notion.baseURL}/{Notion.version}/{url}'
        print(f'[GET] {url}')
        return req.get(url, headers=self.header).json()

    def patch(self, url: str, data: dict) -> dict:
        print(f'[PATCH] {url}')
        return req.patch(url, headers=self.header, data=data)

    class Database:
        def create_database(databaseID: str, *args, **kwargs) -> dict:
            pass

        def update_database(databaseID: str, *args, **kwargs) -> dict:
            pass

        def retrieve_database(notion: Notion, databaseID: str, *args, **kwargs) -> dict:
            return notion.get(f'databases/{databaseID}')

        def query(databaseID: str, *args, **kwargsclea) -> dict:
            pass

    class Page:
        def create_page(databaseID: str, *args, **kwargs) -> dict:
            pass

        def retrive_page(page_id: str, *args, **kwargs) -> str:
            return f'pages/{page_id}'

        def update_page(databaseID: str, *args, **kwargs) -> dict:
            pass

    class Block:
        pass
