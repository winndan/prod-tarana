# directory utils/dbCon.py
import asyncio
from dotenv import load_dotenv
import os
from supabase import create_client, Client

# ✅ Load environment variables
load_dotenv()

# ✅ Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def initialize_supabase():
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("❌ Supabase credentials are missing!")
    return create_client(SUPABASE_URL, SUPABASE_KEY)

dbconnection: Client = initialize_supabase()
