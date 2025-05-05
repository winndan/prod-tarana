# middleware.py

import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse
from auths.backend.jwtUtils import verify_token
from starlette.requests import Request  # Not FastAPI specific

logger = logging.getLogger(__name__)

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Public routes (no auth required)
        PUBLIC_ROUTES = {
            "/", 
            "/signin", 
            "/login", 
            "/auth_redirect",
            "/logout",
            "/search",
            "/explore",
            "/dashboard",
            "/agent",
            "/booking",
            "/assets"  # Base path for static assets
        }
        
        # Skip auth checks for:
        # 1. Public routes
        # 2. Static files (/assets/* or /static/*)
        # 3. Favicon requests
        if (request.url.path in PUBLIC_ROUTES or
            request.url.path.startswith('/assets/') or
            request.url.path.startswith('/static/') or
            request.url.path == '/favicon.ico'):
            return await call_next(request)
            
        # Authentication check for protected routes
        token = request.cookies.get("access_token")
        
        if not token:
            logger.warning(f"Missing token for {request.method} {request.url.path}")
            return RedirectResponse("/signin", status_code=303)
            
        if not verify_token(token):
            logger.warning(f"Invalid token for {request.method} {request.url.path}")
            return RedirectResponse("/signin", status_code=303)
            
        return await call_next(request)
