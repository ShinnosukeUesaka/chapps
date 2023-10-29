from chapps.templates import template
from chapps.state import ConfigChappState, State

import reflex as rx


@template(route="/chappConfig", title="chappConfig", on_load=State.check_logged_in)
def chappConfig() -> rx.Component:
    return configuration()

def configuration():
    return rx.vstack(
        rx.heading("Tool Configuration", font_size="2em", padding ="5"),
        rx.hstack(
            rx.text("Tool Description"),
            rx.input(
                on_change=lambda value:ConfigChappState.edit_short_description(value),
                id="tool_description",
            ),
            rx.button("Confirm", type_="confirm"),
            rx.text(ConfigChappState.unsaved_chapp.short_description),
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(ConfigChappState.description_of_chapp),
    )
