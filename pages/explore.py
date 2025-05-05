from utils.dbCon import dbconnection
from pages.design.navbar import reusable_navbar
from fasthtml.common import *
from monsterui.all import *
from pages.design.components import TripCard, pagination_controls, category_tabs

async def explore_page(page: int = 1, category: str = "", query: str = ""):
    """Explore Page with Pagination and Search (Supabase version)"""
    ITEMS_PER_PAGE = 10

    # --- Build Supabase query ---
    supabase_query = dbconnection.table("trips").select("*")
    if category:
        supabase_query = supabase_query.eq("category", category)
    if query:
        supabase_query = supabase_query.ilike("name", f"%{query}%")

    # --- Pagination ---
    start_idx = (page - 1) * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE - 1

    # --- Get total count for pagination ---
    count_query = dbconnection.table("trips").select("id", count="exact")
    if category:
        count_query = count_query.eq("category", category)
    if query:
        count_query = count_query.ilike("name", f"%{query}%")
    count_data = count_query.execute()
    total_count = count_data.count if hasattr(count_data, "count") else len(count_data.data)
    total_pages = (total_count + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    # --- Fetch paginated data ---
    data = supabase_query.range(start_idx, end_idx).execute()
    trips = data.data if hasattr(data, "data") else data

    # --- Get categories for tabs ---
    cats_data = dbconnection.table("trips").select("category").execute()
    categories = sorted(set(t["category"] for t in cats_data.data))

    # --- Render the page ---
    return Container(
        reusable_navbar(),
        Container(
            DivCentered(
                H1("Discover Amazing Trips!"),
                A(Input(
                    placeholder="Search...",
                    cls="w-3/4 p-2 rounded-lg h-8 border border-gray-300 text-base",
                    id="search-input",
                    name="query",
                    hx_get="/search",
                    hx_target="#trips-section",
                    hx_trigger="input changed delay:300ms",
                    hx_include="[name='query']",
                    value=query
                )),
                id="welcome-section"
            ),
            Div(category_tabs(category, categories), cls="w-full flex justify-center items-center mb-6"),
            Section(
                H2(
                    f"Trips in {category}" if category else "All Trips",
                    cls="text-center text-4xl font-extrabold text-gray-900 bg-gradient-to-r from-[#FF5733] to-[#FFC0CB] text-white py-4 px-8 rounded-xl shadow-lg tracking-wide mb-6"
                ),
                Grid(
                    *[TripCard(t, img_id=i) for i, t in enumerate(trips)],
                    cols_lg=2
                ),
                pagination_controls(page, total_pages, category),
                id="trips-section"
            ),
            cls=(ContainerT.xl, 'uk-container-expand')
        )
    )
