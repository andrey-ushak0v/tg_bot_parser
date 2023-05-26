import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = str(os.getenv('TOKEN'))
API_ID = str(os.getenv('api_id'))
API_HASH = str(os.getenv('api_hash'))
PHONE = str(os.getenv('phone'))