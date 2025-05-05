import logging
from fasthtml.common import *
from monsterui.all import *
from auths.frontend.signInPage import signin_page
from pages.homepage import home
import requests
from dotenv import load_dotenv
import os
from utils.dbCon import dbconnection
import jwt
from datetime import datetime, timedelta
from starlette.responses import JSONResponse, RedirectResponse, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware import Middleware  # Import Middleware wrapper

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

# Config
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = "http://localhost:5001/auth_redirect"

# JWT Functions
def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(hours=24)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        return None

# Cookie Helpers
def set_jwt_cookie(response: Response, token: str):
    response.set_cookie(
        key="access_token",
        value=token,
        max_age=24*3600,
        httponly=True,
        secure=False,  # Set True in production with HTTPS
        samesite="lax"
    )

def remove_jwt_cookie(response: Response):
    response.delete_cookie("access_token")

# Middleware definition
class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Skip auth checks for public routes
        if request.url.path in ["/", "/signin", "/login", "/auth_redirect", "/logout"]:
            return await call_next(request)
            
        token = request.cookies.get("access_token")
        if not token or not verify_token(token):
            logger.warning("Unauthorized access attempt")
            return RedirectResponse("/signin", status_code=303)
            
        return await call_next(request)

# Create FastHTML app with middleware registered the FastHTML way
app, rt = fast_app(
    hdrs=Theme.neutral.headers(daisy=True),
    live=True,
    middleware=[Middleware(JWTMiddleware)]
)

# Routes remain unchanged
@rt("/")
def landingPage():
    logger.info("User visited landing page")
    return home()

@rt("/signin")
def getSignInPage():
    logger.info("User on sign-in page")
    return signin_page(login_url="/login")

@rt("/login")
def login(request):
    if request.cookies.get("access_token"):
        logger.info("User already authenticated")
        return RedirectResponse("/dashboard", status_code=303)
        
    oauth_params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent"
    }
    from urllib.parse import urlencode
    auth_url = f"https://accounts.google.com/o/oauth2/auth?{urlencode(oauth_params)}"
    return RedirectResponse(auth_url, status_code=307)

@rt("/auth_redirect")
def google_callback(request):
    code = request.query_params.get("code")
    if not code:
        return JSONResponse({"error": "Missing code"}, status_code=400)

    try:
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
            return RedirectResponse("/signin", status_code=303)

        access_token = token_resp.json().get("access_token")
        if not access_token:
            return JSONResponse({"error": "Failed to obtain access token"}, status_code=400)

        userinfo = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()

        email = userinfo.get("email")
        if not email:
            return JSONResponse({"error": "Missing email"}, status_code=400)

        try:
            dbconnection.table("users").upsert({
                "email": email,
                "name": userinfo.get("name", "No Name"),
                "google_id": userinfo.get("id", ""),
                "profile_picture": userinfo.get("picture", "")
            }, on_conflict="email").execute()
        except Exception as e:
            logger.error(f"Database error: {e}")
            return JSONResponse({"error": "Database operation failed"}, status_code=500)

        jwt_token = create_access_token({
            "sub": email,
            "name": userinfo.get("name", "No Name")
        })
        
        response = RedirectResponse("/dashboard", status_code=303)
        set_jwt_cookie(response, jwt_token)
        return response

    except Exception as e:
        logger.error(f"Auth error: {e}")
        return JSONResponse({"error": "Authentication failed"}, status_code=500)

@rt("/dashboard")
def dashboard(request):
    token = request.cookies.get("access_token")
    payload = verify_token(token)
    
    if not payload:
        return RedirectResponse("/signin", status_code=303)
        
    return Div(
        H1("Welcome to Your Dashboard"),
        P(f"Logged in as: {payload['sub']}"),
        A("Logout", href="/logout")
    )

@rt("/logout")
def logout():
    response = RedirectResponse("/", status_code=303)
    remove_jwt_cookie(response)
    return response

if __name__ == "__main__":
    logger.info("Starting application")
    serve()
