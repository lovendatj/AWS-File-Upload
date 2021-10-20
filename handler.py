import StandardLibrary.Services.Notion as Notion
from StandardLibrary.Utils.FileData import read_json

NOTION_KEY = read_json('./secret.json')['notion']['key']
DEFAULT_DB = read_json('./secret.json')['notion']['databaseID']


notion = Notion(NOTION_KEY, DEFAULT_DB)
