from chapps.templates import template
from chapps.state import ExploreState, State
from chapps.state import Chapp

import reflex as rx

def display_chapp(chapp: Chapp):
    return rx.box(rx.text(chapp.title))

@template(route="/exploreChapps", title="exploreChapps", on_load=State.check_logged_in)
def exploreChapps() -> rx.Component:
    return rx.vstack(
        rx.heading("search tools", font_size="2em", padding ="5"),
        rx.vstack(
            rx.input(
                placeholder="Tool Description",
                id="tool_description",
                on_change=ExploreState.set_search_query
            ),
            rx.button(
                "Submit", type_="submit", padding ="5",
                on_click=ExploreState.search_chaps()
            ),
            rx.responsive_grid(
                rx.foreach(ExploreState.search_results, display_chapp),
                columns=[2, 4, 6],
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
