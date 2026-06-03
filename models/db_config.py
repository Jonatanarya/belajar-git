import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")

if DB_PASSWORD is None:
    raise ValueError("DB_PASSWORD tidak ditemukan di file .env")

DB_CONFIG = {
    "password": DB_PASSWORD
}