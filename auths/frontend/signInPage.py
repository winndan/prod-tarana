from fasthtml.common import *
from monsterui.all import *

def signin_page(login_url="/login"):
    left = Div(
        cls="col-span-1 hidden flex-col justify-between p-8 text-white lg:flex bg-cover bg-center bg-no-repeat",
        style="background-image: url('/assets/banner-1.jpg');"
    )(
        Div(cls=TextT.bold)("Bukana Hotels"),
        Blockquote(cls="space-y-2")(
            P(cls=TextT.lg)("Login to access your personalized experience..."),
            Footer(cls=TextT.sm)("Sign in now")
        )
    )
    
    right = Div(cls="col-span-2 flex flex-col p-8 lg:col-span-1")(
        DivRAligned(
            Button(
                "Back Home",
                cls=ButtonT.ghost,
                onclick="window.location.href='/'"
            )
        ),
        DivCentered(cls='flex-1')(
            Container(
                DivVStacked(
                    H3("Sign In", cls="text-center"),
                    Small("Enter your credentials...", cls=TextT.muted + " text-center")
                ),
                DivVStacked(cls="w-full flex justify-center")(
                    Button(
                        Span(
                            "G",
                            cls="mr-2 font-bold text-2xl bg-clip-text text-transparent "
                                "bg-[conic-gradient(at_center,_#4285F4_0deg_90deg,_#EA4335_90deg_180deg,_#FBBC05_180deg_270deg,_#34A853_270deg)]"
                        ),
                        "Sign In with Google",
                        cls=ButtonT.default + " w-64",  # Fixed width for better display
                        onclick=f"window.location.href='{login_url}';"
                    ),
                ),
                Div(id="loading-indicator", cls="hidden text-center")(
                    Loading(cls=LoadingT.spinner, htmx_indicator=True)
                ),
                Div(id="toast-container", cls="absolute top-5 right-5"),
                DivVStacked(
                    Small(
                        "By signing in, you agree to our Terms of Service and Privacy Policy",
                        cls=TextT.muted + " text-center"
                    )
                ),
                cls="space-y-6"
            )
        )
    )
    
    return Title("Auth Example"), Grid(left, right, cols=2, gap=0, cls='h-screen')