import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

settings = Settings()