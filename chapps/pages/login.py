import reflex as rx
from chapps.state import State

@rx.page(route="/login", title="Login")
def login():
    return rx.vstack(
        rx.input(
        placeholder="Enter your username",
        id="username",
        on_blur=State.set_username,
        ),
        rx.link(
            rx.button("Login", type_="confirm", on_click=State.create_user_or_login),
            href='/',
        )
    )
