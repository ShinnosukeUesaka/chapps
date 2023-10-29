"""The home page of the app."""

from chapps import styles
from chapps.templates import template
from chapps.state import State, HomeState, Chapp

import reflex as rx


@rx.page(route="/", title="Home", image="/github.svg", on_load=[State.check_logged_in, HomeState.get_chapps])
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.flex(
        rx.link(rx.text("Explore"), href="/explore"),
        main_content(),
        rx.link(rx.text("CreateNew"), href="/create"),
        rx.button(
            rx.icon(tag="moon"),
            on_click=rx.toggle_color_mode,
        ),
    )

def chapp_card(chapp: Chapp):
    return rx.box(
        rx.center(
            rx.link(
                rx.heading(chapp.title, font_size="2em"),
                href=f"/chapp/{chapp.id}",
            )
        ),
        height="5em", width="5em", bg="lightgreen"
    )

def main_content():
    return rx.responsive_grid(
        rx.foreach(HomeState.my_chapps, chapp_card),
        columns=[2, 3],
        spacing="4",
    )
