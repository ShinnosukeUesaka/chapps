import reflex as rx
from chapps.state import State, RunChappState
from chapps.styles import *

@rx.page(route="/chapp/[chapp_id]", title="Chapp", on_load=RunChappState.get_chapp)
def chapp_screen() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.image(src="/robo.jpg", width="auto", height = "50%"),
            rx.heading(RunChappState.chapp.title),
            rx.text(RunChappState.chapp.description),
            width = "45%", padding = 4
        ),
        rx.vstack(
            rx.flex(
                rx.box(width = "90%"),
                rx.image(src="/home.png", width="auto", height = "8"),
                width = "100%", padding = 5,
            ),
            rx.flex(
                rx.vstack(
                    rx.heading("Input:"),
                    rx.divider(height = 10),
                    rx.ordered_list(
                        rx.foreach(RunChappState.chapp.inputs, input_field),
                        rx.divider(height = 10, ),
                        rx.button("Run", type_="confirm", on_click=RunChappState.run_chapp(), style = button_style),
                    ),
                    padding = 7, align_items = "normal"
                ),
                rx.vstack(
                    rx.heading("Output:"),
                    rx.divider(height = 10),
                    rx.text(RunChappState.output),
                    width = "70%",
                    padding = 7,
                    align_items = "normal"
                ),
                width = "90%",
            ),
            width = "55%"
            
        )
    )

def input_field(input):
    return rx.vstack(
        rx.text(input.name),
        rx.input(
            placeholder=input.description,
            on_blur=lambda value: RunChappState.set_input(input.name, value),
        ),
    )