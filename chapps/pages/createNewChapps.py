from chapps.templates import template
from chapps.state import FormState

import reflex as rx


@template(route="/createNewChapps", title="CreateNewChapps")
def createNewChapps() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("What do tools do you want to create", font_size="3em", padding ="5"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Tool Description",
                    id="tool_description",
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=FormState.handle_submit,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )