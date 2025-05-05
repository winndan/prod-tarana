from fasthtml.common import *
from monsterui.all import *
from pages.design.navbar import reusable_navbar
from utils.dbCon import dbconnection


def Tags(cats):
    """Render a list of category labels."""
    return DivLAligned(map(Label, cats))


def get_user_bookings():
    """Fetch user bookings from Supabase with error handling."""
    response = dbconnection.table("bookings").select("*").execute()
    # Supabase client response may not have 'error' attribute depending on version,
    # so we check if data is None or empty as a simple error check.
    if response.data is None:
        raise Exception("Error fetching bookings: No data returned from Supabase.")
    return response.data  # List of booking dicts



def booking():
    """Booking Page route handler."""
    try:
        bookings = get_user_bookings()
    except Exception as e:
        # Render an error page or message if fetching fails
        return Container(
            reusable_navbar(),
            DivCentered(H1("Booking Page - Error")),
            DivCentered(P(f"Failed to load bookings: {str(e)}"))
        )

    booking_cards = [
        Card(
            DivLAligned(
                A(
                    Img(
                        src=f"https://picsum.photos/200/200?random={booking['id']}",
                        style="width:200px"
                    ),
                    href="#"
                ),
                Div(cls='space-y-3 uk-width-expand')(
                    H4(booking["guest_name"]),
                    P(f"Room Number: {booking['room_number']}"),
                    P(f"Check-in: {booking['check_in_date']}"),
                    P(f"Check-out: {booking['check_out_date']}"),
                    P(f"Guests: {booking['number_of_guests']}"),
                    P(Strong(f"${booking['total_price']:.2f}"), cls=TextT.sm),
                    P(f"Status: {booking['status']}", cls=TextT.muted),
                    DivFullySpaced(
                        Tags(
                            [booking["payment_method"]] +
                            ([booking.get("reference_number", "N/A")] if booking["payment_method"] == "eCash" else [])
                        ),
                        Button(
                            "View Details",
                            cls=(ButtonT.primary, 'h-6'),
                            on_click=f"/booking/{booking['id']}"
                        )
                    )
                )
            ),
            cls=CardT.hover
        )
        for booking in bookings
    ]

    return Container(
        reusable_navbar(),
        DivCentered(
            H1(
                "Booking Page",
                cls="text-center text-4xl font-extrabold text-gray-900 "
                    "bg-gradient-to-r from-[#FF5733] to-[#FFC0CB] text-white "
                    "py-4 px-8 rounded-xl shadow-lg tracking-wide mb-6"
            )
        ),
        DivCentered(
            P("Here you can manage your trip bookings.", cls="mb-6")
        ),
        Div(
            *booking_cards,
            cls="mt-6"
        )
    )
