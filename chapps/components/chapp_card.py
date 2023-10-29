import reflex as rx
from chapps.state import Chapp

def chapp_card(chapp: Chapp):
    return rx.box(
        rx.center(
            rx.link(
                rx.heading(chapp.title, font_size="2em"),
                href=f"/chapp/{chapp.id}",
            )
        ),
        height="15em", width="15em", bg="lightgreen"
    )
