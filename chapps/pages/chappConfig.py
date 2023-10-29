from chapps.templates import template
from chapps.state import CreateNewState
from chapps.state import CreateNewState

import reflex as rx


@template(route="/chappConfig", title="chappConfig")
def chappConfig() -> rx.Component:
    return rx.vstack(
        rx.heading("Tool Configuration", font_size="2em", padding ="5"),
        rx.hstack(
            rx.text("Tool Description"),
            rx.input(
                on_change=lambda value:CreateNewState.edit_short_description(value),
                id="tool_description",
            ),
            rx.button("Confirm", type_="confirm"),
            rx.text(CreateNewState.chapp.short_description),
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(CreateNewState.description_of_chapp),
    )
