import os
from db_schema import db_schema
import requests
import json
from dotenv import load_dotenv,find_dotenv
from populate_db import populate_db

load_dotenv(find_dotenv("./private/.env"))
def create_db():
    NOTION_PAGE_ID=os.environ.get("NOTION_PAGE_ID")
    body={
        "parent":{"type":"page_id","page_id":NOTION_PAGE_ID},
        "title":[{
            "type":"text",
            "text":{"content":"Notes To Notion"},
        }],
        "is_inline":True
    }
    body["properties"]=db_schema
    NOTION_SECRET=os.environ.get("NOTION_SECRET")
    headers={
        "Authorization":f'Bearer {NOTION_SECRET}',
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Notion-Version":"2022-06-28",
    }
    res = requests.post(f'https://api.notion.com/v1/databases',json=body,headers=headers)
    # print(json.dumps(json.loads(res.text),indent=4))
    res_json = res.json()
    if("id" in res_json):
        print(res_json)
        db_file = open("./private/notion_db_id.txt","w")
        db_file.write(f'DATABASE_ID: {res_json["id"]}')
        db_file.close()
        if (os.path.exists("./private/notion_db_id.txt")):
            populate_db()
