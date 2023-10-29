"""The home page of the app."""

from chapps import styles
from chapps.templates import template
from chapps.state import State, HomeState, Chapp, ConfigChappState, ExploreState
from chapps.styles import *


import reflex as rx


@rx.page(route="/", title="Home", image="/github.svg", on_load=[State.check_logged_in, HomeState.get_chapps])
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.flex(
        rx.cond(
            State.explore_toggled,
            rx.button("Libary", on_click=State.toggle_explore),
            rx.button("Explore", on_click=State.toggle_explore),
        ),
        rx.cond(
            State.explore_toggled,
            explore_page(), library_page(),
        ),
        rx.button(
            rx.icon(tag="moon"),
            on_click=rx.toggle_color_mode,
        ),
        create_new_chapp_sidebar(),
    )

def create_new_chapp_sidebar():
    return  rx.vstack(
        rx.heading("What do tools do you want to create", font_size="3em", padding ="5", style = header_style),
        rx.vstack(
            rx.input(
                placeholder="Tool Description",
                on_change=ConfigChappState.set_description_of_chapp,
                id="tool_description",
                style = inp_style,
                padding = "3",
            ),
            rx.button("Submit", type_="confirm", on_click=ConfigChappState.create_chapp(), style = submit_style),
        ),
    )

def explore_page():
    return rx.vstack(
        rx.heading("Explore", font_size="2em", padding ="5"),
        rx.text("Explore Chapps other people have made"),
        rx.input(
            placeholder="Tool Description",
            id="tool_description",
            value=ExploreState.search_query,
            on_change=ExploreState.set_search_query
        ),
        rx.button(
            "Submit", type_="submit", padding ="5",
            on_click=ExploreState.search_chaps
        ),
        chapp_grid(ExploreState.search_results),
    )

def library_page():
    return rx.vstack(
        rx.heading("Libary", font_size="2em", padding ="5"),
        chapp_grid(HomeState.my_chapps),
    )

def chapp_card(chapp: Chapp):
    return rx.box(
        rx.center(
            rx.link(
                rx.heading(chapp.title, font_size="2em"),
                href=f"/chapp/{chapp.id}",
            )
        ),
        height="15em", width="15em", bg="lightgreen",style = card_style,
    )

def chapp_grid(chapps: list[Chapp]) -> rx.Component:
    return rx.responsive_grid(
        rx.foreach(chapps, chapp_card),
        columns=[2, 3],
        spacing="20",
    )
