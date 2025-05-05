import os
import jwt
from datetime import datetime, timedelta
from starlette.responses import Response

# Load secrets from environment
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

def create_access_token(data: dict, expires_delta: int = 24*3600):
    """
    Create a JWT access token with an expiration (default: 24 hours).
    """
    expire = datetime.utcnow() + timedelta(seconds=expires_delta)
    data = data.copy()
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    """
    Decode and verify a JWT token. Returns payload or None if invalid/expired.
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Token is invalid
        return None

def set_jwt_cookie(response: Response, token: str):
    """
    Set the JWT as a secure, HTTP-only cookie.
    """
    response.set_cookie(
        key="access_token",
        value=token,
        max_age=24*3600,
        httponly=True,
        secure=False,  # Set True in production!
        samesite="lax"
    )

def remove_jwt_cookie(response: Response):
    """
    Remove the JWT cookie from the response.
    """
    response.delete_cookie("access_token")
