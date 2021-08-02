import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')

host = os.getenv('host')
port = os.getenv('port')
db = os.getenv('db')
db_user = os.getenv('db_user')
db_pass = os.getenv('db_pass')

url = f'postgresql://{db_user}:{db_pass}@{host}:{port}/{db}'
