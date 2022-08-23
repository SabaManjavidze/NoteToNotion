from asyncio.windows_events import NULL
import json
import os
import requests
from format_pushups import format_pushups
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv("./private/.env"))
def populate_db():
    if (os.path.exists("./private/notion_db_id.txt")==False):
        return
    db_file=open("./private/notion_db_id.txt","r")
    if(db_file == NULL):return
    notion_db_id=db_file.readlines()[0].split("DATABASE_ID: ")[1]
    body={
        "parent":{"type":"database_id","database_id":notion_db_id},
    }
    db_file.close()
    entries=format_pushups()
    for index,entry in enumerate(entries):
        body["properties"]=entry
        NOTION_SECRET=os.environ.get("NOTION_SECRET")
        headers={
            "Authorization":f'Bearer {NOTION_SECRET}',
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Notion-Version":"2022-06-28",
        }
        res = requests.post(f'https://api.notion.com/v1/pages',json=body,headers=headers)
        print(json.dumps(res.json(),indent=4))
populate_db()