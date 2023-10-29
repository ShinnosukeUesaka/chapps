from chapps.templates import template
from chapps.state import ConfigChappState, State

import reflex as rx


@template(route="/chappConfig", title="chappConfig", on_load=State.check_logged_in)
def chappConfig() -> rx.Component:
    return configuration()

def configuration():
    return rx.vstack(
        rx.heading("Tool Configuration", font_size="2em", padding ="5"),
        rx.flex(
            rx.vstack(
                rx.text("Title"),
                rx.input(
                    value=ConfigChappState.unsaved_chapp.title,
                    on_change=lambda value:ConfigChappState.edit_title(value),
                    id="tool_title",
                ),
                rx.text("Tool Description"),
                rx.input(
                    value=ConfigChappState.unsaved_chapp.short_description,
                    on_change=lambda value:ConfigChappState.edit_short_description(value),
                    id="tool_description",
                ),
                rx.text("Tool Inputs"),
                rx.foreach(ConfigChappState.unsaved_chapp.inputs, input_field),

                rx.text("Tool Instruction"),
                rx.input(
                    value=ConfigChappState.unsaved_chapp.instruction,
                    on_change=lambda value:ConfigChappState.edit_instruction(value),
                    id="tool_instruction",
                ),
                rx.button("Confirm", on_click=ConfigChappState.save_chapp()),
            ),

            rx.vstack(
                rx.input(
                    value=ConfigChappState.unsaved_chapp.examples[0].output,
                    on_change=lambda value:ConfigChappState.edit_examples(value),
                    id="tool_description",
                ),
            )
        ),

        rx.divider(),
        rx.heading("Results"),
        rx.text(ConfigChappState.description_of_chapp),
        rx.button("Confirm", type_="confirm", on_click=ConfigChappState.save_chapp()),
    )

def input_field(input):
    return rx.vstack(
        rx.text(input.name),
        rx.input(
            placeholder=input.name,
            on_blur=lambda value: ConfigChappState.edit_inputs(value),
        ),
    )
