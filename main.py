import logging
from fasthtml.common import *
from monsterui.all import *
from auths.frontend.signInPage import signin_page
from pages.homepage import home
from dotenv import load_dotenv
import os

from starlette.responses import JSONResponse, RedirectResponse, Response
from starlette.middleware import Middleware

# --- External Imports ---
from auths.backend.googleCallback import handle_google_callback
from auths.backend.googleOauth import (
    GOOGLE_CLIENT_ID,
    GOOGLE_REDIRECT_URI,
    get_google_oauth_login_url,
)
from auths.backend.jwtUtils import (
    create_access_token,
    verify_token,
    set_jwt_cookie,
    remove_jwt_cookie,
)
from middleware import JWTMiddleware

from pages.profile import profile_page
from pages.explore import explore_page
from utils.dbCon import dbconnection
from pages.design.components import TripCard, pagination_controls, category_tabs
from pages.booking import get_user_bookings, booking


# --- Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

# --- App Setup ---
app, rt = fast_app(
    hdrs=Theme.neutral.headers(daisy=True),
    live=True,
    middleware=[Middleware(JWTMiddleware)]
)

# --- Routes ---
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
        return RedirectResponse("/dashboard", status_code=303)
    auth_url = get_google_oauth_login_url()
    return RedirectResponse(auth_url, status_code=307)

@rt("/auth_redirect")
def google_callback(request):
    return handle_google_callback(request, set_jwt_cookie)

@rt("/dashboard")
def dashboard(request):
    token = request.cookies.get("access_token")
    payload = verify_token(token)
    return profile_page(payload)

@rt("/search")
async def search(request):
    query = request.query_params.get("query", "")
    # Fetch matching trips from Supabase
    supabase_query = dbconnection.table("trips").select("*")
    if query:
        supabase_query = supabase_query.ilike("name", f"%{query}%")
    data = supabase_query.execute()
    trips = data.data if hasattr(data, "data") else data

    if not trips:
        return Div(
            DivCentered(
                H3("No trips found.", cls="text-xl text-gray-500 my-8"),
                Img(src="https://cdn-icons-png.flaticon.com/512/7486/7486790.png", cls="mx-auto", width=120, height=120, alt="No results")
            ),
            cls="uk-grid-match"
        )

    return Div(
        *[TripCard(t, img_id=i) for i, t in enumerate(trips)],
        cls="uk-grid-match"
    )


@rt("/explore")
async def explore(request):
    page = int(request.query_params.get("page", 1))
    category = request.query_params.get("category", "")
    query = request.query_params.get("query", "")
    return await explore_page(page=page, category=category, query=query)


@rt("/booking")
def booking_page():
    return booking()


@rt("/logout", methods=["POST"])
def logout():
    response = Response()
    remove_jwt_cookie(response)  # your function to clear auth cookie
    response.headers["HX-Redirect"] = "/"
    return response

if __name__ == "__main__":
    logger.info("Starting application")
    serve()
