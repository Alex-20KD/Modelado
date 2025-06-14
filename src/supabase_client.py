import os
from supabase import create_client
from dotenv import load_dotenv
from pathlib import Path # 1. Importa la clase Path

env_path = Path(__file__).parent.parent / '.env'

load_dotenv(dotenv_path=env_path)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

