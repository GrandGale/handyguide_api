import os
from pathlib import Path


DEBUG = True
SESSION = "2022_2023"

BASE_DIR = str(Path(__name__).resolve().parent)
MEDIA_DIR = os.path.join(BASE_DIR, "media")
