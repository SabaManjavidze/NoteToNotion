import os
from dotenv import load_dotenv,find_dotenv
import requests

load_dotenv(find_dotenv("./private/.env"))
def update_db_schema():
    body={
        "properties": {
            "Total Push Ups":{
                "type":"number",
                "number":{}
            }
        }
    }
    # body["properties"]=db_schema
    NOTION_SECRET=os.environ.get("NOTION_SECRET")
    headers={
        "Authorization":f'Bearer {NOTION_SECRET}',
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Notion-Version":"2022-06-28",
    }
    file=open("./private/notion_db_id.txt","r")
    NOTION_DB_ID=file.readlines()[0].split("DATABASE_ID: ")[1]
    res = requests.patch(f'https://api.notion.com/v1/databases/{NOTION_DB_ID}',json=body,headers=headers)
    file.close()