"""The dashboard page."""
from chapps.templates import template

import reflex as rx
from chapps.state import State


@template(route="/dashboard", title="Dashboard", on_load=State.check_logged_in)
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Dashboard", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/dashboard.py"),
        ),
    )
