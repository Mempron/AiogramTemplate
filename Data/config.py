import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
admin = int(os.getenv('ADMIN_ID'))
