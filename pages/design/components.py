# pages/components.py
from fasthtml.common import *
from monsterui.all import *

# --- COMPONENTS (copy these to the top of pages/explore.py or import from components.py) ---

def TripCard(t, img_id=1):
    return Card(
        PicSumImg(w=500, height=100, id=img_id),
        DivFullySpaced(
            H4(t["name"]),
            P(Strong(t["price"], cls=TextT.sm)),
            P(Em(t["category"], cls=TextT.xs, style="color: gray; font-weight: bold;"))
        ),
        Button("Details", cls=(ButtonT.primary, "w-full"))
    )

def category_tabs(active_category, categories):
    return TabContainer(
        *[
            Li(
                A(
                    cat,
                    href=f"/?category={cat}",
                    cls=('uk-active uk-text-bold uk-text-primary' if cat == active_category else 'uk-text-muted'),
                    style="border-bottom: 2px solid black;" if cat == active_category else ""
                )
            )
            for cat in categories
        ]
    )

def pagination_controls(page, total_pages, category):
    return DivCentered(
        Div(
            A("← Prev", href=f"/?page={page - 1}&category={category}" if page > 1 else "#", cls=ButtonT.primary if page > 1 else "uk-disabled"),
            Span(f" Page {page} of {total_pages} ", cls="uk-text-bold uk-margin-small"),
            A("Next →", href=f"/?page={page + 1}&category={category}" if page < total_pages else "#", cls=ButtonT.primary if page < total_pages else "uk-disabled"),
            cls="uk-flex uk-flex-center uk-gap-small uk-margin-large"
        )
    )
