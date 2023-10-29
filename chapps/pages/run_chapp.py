import reflex as rx
from chapps.state import State, RunChappState, ConfigChappState

@rx.page(route="/chapp/[chapp_id]", title="Chapp", on_load=RunChappState.get_chapp)
def chapp_screen() -> rx.Component:
    return rx.vstack(
        rx.heading(RunChappState.chapp.title),
        rx.text(RunChappState.chapp.description),
        rx.foreach(RunChappState.chapp.inputs, input_field),
        rx.button("Run", type_="confirm", on_click=RunChappState.run_chapp()),
        rx.heading("Output:"),
        rx.text(RunChappState.output),
        rx.button("Edit", type_="confirm", on_click=ConfigChappState.edit_chapp(RunChappState.chapp.id)),
    )

def input_field(input):
    return rx.vstack(
        rx.text(input.name),
        rx.input(
            placeholder=input.description,
            on_blur=lambda value: RunChappState.set_input(input.name, value),
        ),
    )
