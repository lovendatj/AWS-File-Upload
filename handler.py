from StandardLibrary.Services.Notion import Notion
from StandardLibrary.Utils.FileData import read_json

NOTION_KEY = read_json('./secret.json')['notion']['key']


notion = Notion(auth=NOTION_KEY)
dbo = Notion.Database.retrieve_database(
    notion=notion, databaseID="c4d02233c9a84d76b2b52271228bd25f")
dbi, properties = dbo['id'], dbo['properties']

print(f'Retrieved: {dbo["title"][0]["text"]["content"]} - {dbi}')
for key, val in properties.items():
    print(f'{key}: {val["id"]}')
