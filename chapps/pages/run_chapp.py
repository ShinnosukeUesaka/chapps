import reflex as rx
from chapps.state import State, RunChappState, ConfigChappState

from chapps.styles import *


@rx.page(route="/chapp/[chapp_id]", title="Chapp", on_load=RunChappState.get_chapp)
def chapp_screen() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.image(src="/robo.jpg", width="auto", height="50%"),
            rx.heading(RunChappState.chapp.title, ),
            rx.text(RunChappState.chapp.description, width="90%"),
            width="45%",
            padding=4,
            background_color="#EAF0F3",
            #shadow on the right
            box_shadow="4px 4px 15px 8px #C8CED6",
            z_index="100",
        ),
        rx.vstack(
            rx.flex(
                rx.box(width="90%"),
                rx.image(src="/home.png", width="auto", height="8"),
                width="100%",
                padding=5,
            ),
            rx.flex(
                rx.vstack(
                    rx.box(
                        rx.heading("Input"),
                        rx.divider(height=10),
                        rx.foreach(RunChappState.chapp.inputs, input_field),
                        align_items="left",
                    ),
                    rx.divider(
                        height=10,
                    ),
                    rx.button(
                        "Run",
                        type_="confirm",
                        on_click=RunChappState.run_chapp(),
                        style=button_style,
                    ),
                    padding=7,
                ),
                rx.vstack(
                    rx.heading("Output"),
                    rx.divider(height=10),
                    rx.text(RunChappState.output),
                    rx.divider(height=10),
                    rx.button(
                        "Edit",
                        type_="confirm",
                        on_click=ConfigChappState.edit_chapp(RunChappState.chapp.id),
                        style=button_style,
                    ),
                    width="70%",
                    padding=7,
                    align_items="left",
                ),
                width="90%",
            ),
            width="55%",
            background_color="#E1E8F0",
        ),
    )


def input_field(input):
    return rx.vstack(
        rx.text(input.name, text_align="left", width="100%"),
        rx.input(
            placeholder=input.description,
            on_blur=lambda value: RunChappState.set_input(input.name, value),
            box_shadow="4px 4px 8px 4px #FFFFFF, -4px -4px 8px 4px #C8CED6"
        ),
        aling_items="left",
    )
