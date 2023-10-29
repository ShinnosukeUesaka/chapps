from chapps.templates import template
from chapps.state import ExploreState, State
from chapps.state import Chapp
from chapps.components.chapp_card import chapp_card
import reflex as rx




@rx.page(route="/explore", title="exploreChapps", on_load=State.check_logged_in)
def exploreChapps() -> rx.Component:
    return rx.hstack(
            rx.link(rx.text("New"), href="/create"),
            main_content(),
            rx.link(rx.text("Home"), href="/"),
    )

def main_content():
    return rx.vstack(
        rx.heading("search toolss", font_size="2em", padding ="5"),
        rx.vstack(
            rx.input(
                placeholder="Tool Description",
                id="tool_description",
                on_change=ExploreState.set_search_query
            ),
            rx.button(
                "Submit", type_="submit", padding ="5",
                on_click=ExploreState.search_chaps
            ),
            rx.responsive_grid(
                rx.foreach(ExploreState.search_results, chapp_card),
                columns=[2, 3],
            ),
        ),
        #rx.box(rx.foreach(State.chats[State.current_chat], "ji")),
        py="8",
        flex="1",
        width="100%",
        max_w="3xl",
        padding_x="4",
        align_self="center",
        overflow="hidden",
        padding_bottom="5em",
    )
