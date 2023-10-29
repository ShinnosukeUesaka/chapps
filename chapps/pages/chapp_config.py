from chapps.templates import template
from chapps.state import ConfigChappState, State

import reflex as rx


@rx.page(route="/chappConfig", title="chappConfig", on_load=State.check_logged_in)
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
                rx.text("How to use this tool"),
                rx.input(
                    value=ConfigChappState.unsaved_chapp.description,
                    on_change=lambda value:ConfigChappState.edit_description(value),
                    id="tool_description",
                ),
                rx.checkbox("User PDF to provide knowledge.", is_checked=ConfigChappState.unsaved_chapp.rag, on_change=lambda value: ConfigChappState.toggle_rag(value)),
                rx.cond(
                    ConfigChappState.unsaved_chapp.rag,
                    rx.box(
                        rx.input(
                            value=ConfigChappState.unsaved_chapp.pdf_description,
                            on_change=lambda value:ConfigChappState.edit_pdf_description(value),
                            id="tool_rag_pdf",
                        ),
                        rx.upload(
                            rx.text(
                                "Drag and drop files here or click to select files"
                            ),
                            border="1px dotted rgb(107,99,246)",
                            padding="5em",
                            multiple=False,
                            accept={
                                "application/pdf": [".pdf"],
                            },
                        ),
                        rx.button(
                            "Upload",
                            on_click=lambda: ConfigChappState.handle_upload(
                                rx.upload_files()
                            ),
                        ),
                    ),
                ),
                rx.hstack(
                    rx.text("Tool Inputs"),
                    rx.button("Add Input", on_click=ConfigChappState.add_input()),
                ),
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
                rx.heading("Examples"),
            )
                    )

        ),

def input_field(input):
    return rx.hstack(
        rx.input(
            value=input.name,
            on_change=lambda value: ConfigChappState.edit_input_name(value, input.description),
        ),
        rx.text(": "),
        rx.input(
            value=input.description,
            on_change=lambda value: ConfigChappState.edit_input_description(value, input.name),
        ),
        rx.button("Delete", on_click=ConfigChappState.delete_input(input.name)),
    )
