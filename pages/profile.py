from fasthtml.common import *
from monsterui.all import *
from pages.design.navbar import reusable_navbar


def profile_page(payload):
    user_data = payload or {}

    # Helper function to get profile picture URL or fallback avatar
    def get_profile_picture_url(user_data):
        pic = user_data.get('profilePicture')
        if pic and pic.strip():
            return pic
        initials = user_data.get("fullName") or "Guest"
        # Use Dicebear API to generate avatar with initials
        return f'https://avatars.dicebear.com/api/initials/{initials}.svg'

    def FormSectionDiv(*c, cls='space-y-2', **kwargs):
        return Div(*c, cls=cls, **kwargs)

    def FormLayout(title, subtitle, *content, cls='space-y-3 mt-4'):
        return Container(
            Div(
                H3(title),
                Subtitle(subtitle, cls="text-primary"),
                DividerLine(),
                Form(*content, cls=cls)
            )
        )

    def profile_form():
        content = (
            FormSectionDiv(
                LabelInput(
                    "Username",
                    placeholder='sveltecult',
                    id='username',
                    value=user_data.get('fullName', '')
                ),
                P("This is your public display name.", cls="text-primary")
            ),
            FormSectionDiv(
                FormLabel("Email"),
                Input(value=user_data.get('email', ''), readonly=True),
                P("This is your registered email address.", cls="text-primary")
            ),
            FormSectionDiv(
                FormLabel("Profile Picture"),
                Img(
                    src=get_profile_picture_url(user_data),
                    cls="rounded-full object-cover",
                    height=96,
                    width=96,
                    alt="Profile Picture"
                ),
                P("This profile picture is fetched from your Google account.", cls="text-primary")
            )
        )
        return FormLayout(
            'Profile',
            'This is how others will see you.',
            *content
        )

    return Container(
        reusable_navbar(),
        DivCentered(
            profile_form()
        )
    )
