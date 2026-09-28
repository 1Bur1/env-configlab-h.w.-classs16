import os

from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

API_KEY = os.getenv("API_KEY")  # key no longer hardcoded here
