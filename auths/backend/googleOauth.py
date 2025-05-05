# auths/backend/googleOauth.py

import os
import requests
import jwt
from datetime import datetime, timedelta
from utils.dbCon import dbconnection
import logging
from urllib.parse import urlencode

logger = logging.getLogger(__name__)

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:5001/auth_redirect")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(hours=24)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def exchange_code_for_token(code: str):
    token_resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "code": code,
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "redirect_uri": GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code"
        }
    )
    if token_resp.status_code != 200:
        logger.error(f"Token exchange failed: {token_resp.text}")
        return None
    return token_resp.json()

def fetch_userinfo(access_token: str):
    userinfo_resp = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    if userinfo_resp.status_code != 200:
        logger.error(f"Failed to fetch user info: {userinfo_resp.text}")
        return None
    return userinfo_resp.json()

def upsert_user(userinfo: dict):
    try:
        response = dbconnection.table("users").upsert({
            "email": userinfo.get("email"),
            "name": userinfo.get("name", "No Name"),
            "google_id": userinfo.get("id", ""),
            "profile_picture": userinfo.get("picture", "")
        }, on_conflict="email").execute()
        if response.data is None:
            logger.error("Database operation failed.")
            return False
        return True
    except Exception as e:
        logger.exception(f"Exception during upsert: {e}")
        return False

def get_google_oauth_login_url():
    """
    Build the Google OAuth login URL with required parameters.
    """
    oauth_params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent"
    }
    return f"https://accounts.google.com/o/oauth2/auth?{urlencode(oauth_params)}"
