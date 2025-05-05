# navbar.py
from fasthtml.common import *
from monsterui.all import *

def reusable_navbar():
    """Reusable NavBar component"""
    scrollspy_links = (
        A("Profile", href="/dashboard"),
        A("Explore", href="/explore"),
        A("Booking", href="/booking"),
        Button("Logout", hx_post="/logout", hx_swap="none", cls=ButtonT.destructive)
    )
    
    return NavBar(
        *scrollspy_links,
        brand=DivLAligned(H3("Trip Explorer"), 
                          Img(src='assets/logo.png', alt='Coinsumer Logo', cls='logo-img', height=70, width=70)),
        sticky=True, uk_scrollspy_nav=True,
        scrollspy_cls=ScrollspyT.bold
    )