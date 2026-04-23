import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME", "evidences")


settings = Settings()

print("AZURE_CONNECTION_STRING =", settings.AZURE_CONNECTION_STRING)
