from chapps.templates import template
from chapps.state import ConfigChappState, State

import reflex as rx
from chapps.styles import *


@template(route="/createNewChapps", title="CreateNewChapps", on_load=State.check_logged_in)
def createNewChapps() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.cond(
        ConfigChappState.generating_chapp,
        loading_screen(), create_chapp(),
    )

def create_chapp():
    return rx.vstack(
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
        padding = "5"
    )

def loading_screen():
    return rx.vstack(rx.text("Generating a Chapp..."), rx.progress(is_indeterminate=True, width="100%"))
