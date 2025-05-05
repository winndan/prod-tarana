# auths/backend/google_callback_handler.py

from starlette.responses import JSONResponse, RedirectResponse
from auths.backend.googleOauth import exchange_code_for_token, fetch_userinfo, upsert_user
from auths.backend.jwtUtils import create_access_token

def handle_google_callback(request, set_jwt_cookie):
    code = request.query_params.get("code")
    if not code:
        return JSONResponse({"error": "Missing code"}, status_code=400)

    tokens = exchange_code_for_token(code)
    if not tokens:
        return RedirectResponse("/signin", status_code=303)

    access_token = tokens.get("access_token")
    if not access_token:
        return JSONResponse({"error": "Failed to obtain access token"}, status_code=400)

    userinfo = fetch_userinfo(access_token)
    # Proceed with the rest of your logic
    if not userinfo or not userinfo.get("email"):
        return JSONResponse({"error": "Missing required user info"}, status_code=400)

    # Debug: Print out userinfo
    print(f"Google User Info: {userinfo}")

    if not upsert_user(userinfo):
        return JSONResponse({"error": "Database operation failed"}, status_code=500)

    jwt_token = create_access_token({
    "sub": userinfo["email"],
    "fullName": userinfo.get("name", "No Name"),
    "email": userinfo.get("email", ""),
    "profilePicture": userinfo.get("picture", "") 
    })

    # Debug: Print out JWT content
    print(f"JWT Token Payload: {jwt_token}")


    response = RedirectResponse("/dashboard", status_code=303)
    set_jwt_cookie(response, jwt_token)
    return response
