from dotenv import load_dotenv
import os


def get_db_url():
    load_dotenv()
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    db_host = os.environ.get("DB_HOST", default="localhost")
    db_port = os.environ.get("DB_PORT", default=7687)
    return f"bolt://{user}:{password}@{db_host}:{db_port}"
