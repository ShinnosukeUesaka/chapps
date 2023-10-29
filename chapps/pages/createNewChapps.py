from chapps.templates import template
from chapps.state import CreateNewState

import reflex as rx


@template(route="/createNewChapps", title="CreateNewChapps")
def createNewChapps() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("What do tools do you want to create", font_size="3em", padding ="5"),
        rx.vstack(
            rx.input(
                placeholder="Tool Description",
                on_change=CreateNewState.set_description_of_chapp,
                id="tool_description",
            ),
            rx.link(
                rx.button("Submit", type_="submit"),
                href="/chappConfig",
            )
            
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(CreateNewState.description_of_chapp),
    )
