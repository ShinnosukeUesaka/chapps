"""The home page of the app."""

from chapps import styles
from chapps.templates import template
from chapps.state import State, HomeState

import reflex as rx


@rx.page(route="/", title="Home", image="/github.svg", on_load=State.check_logged_in)
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.hstack(
        rx.link(rx.text("Explore"), href="/explore"),
        main_content(),
        rx.link(rx.text("CreateNew"), href="/create"),
    )
def main_content():
    return rx.text("Place holder")
