from create_db import create_db
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv("./private/.env"))


create_db()