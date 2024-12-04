import os
from dotenv import load_dotenv

# TODO: Написать комментарии
load_dotenv()

DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_NAME = os.getenv("DATABASE_NAME")
DB_USER = os.getenv("DATABASE_USER")
DB_PORT = os.getenv("DATABASE_PORT")

