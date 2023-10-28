from chapps.templates import template
from chapps.state import FormState
from chapps.state import State

import reflex as rx

@template(route="/exploreChapps", title="exploreChapps")
def exploreChapps() -> rx.Component:
    return rx.vstack(
        rx.heading("search tools", font_size="2em", padding ="5"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Tool Description",
                    id="tool_description",
                ),
                rx.button("Submit", type_="submit", padding ="5"),
            ),
            on_submit=FormState.handle_submit,
        ),
        rx.box(rx.foreach(State.chats[State.current_chat], "ji")),
        py="8",
        flex="1",
        width="100%",
        max_w="3xl",
        padding_x="4",
        align_self="center",
        overflow="hidden",
        padding_bottom="5em",
    )