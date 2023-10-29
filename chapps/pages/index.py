"""The home page of the app."""

from chapps import styles
from chapps.templates import template
from chapps.state import State, HomeState, Chapp, ConfigChappState, ExploreState
from chapps.styles import *


import reflex as rx


@rx.page(route="/", title="Home", image="/github.svg", on_load=[State.check_logged_in, HomeState.get_chapps])
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.cond(
        ConfigChappState.generating_chapp,
        rx.box(
            rx.progress(is_indeterminate=True, width="100%", position='absolute', z_value=1),
            rx.image(src='/loading_page_bg.png', width='auto', height='1080', z_value=0),
        background_color = '#EAF0F3',
        ),
        main_screen(),
    )


def main_screen():
    return rx.flex(
        rx.hstack(
            rx.cond(
                State.explore_toggled,
                rx.button("Library", on_click=State.toggle_explore),
                rx.button("Explore", on_click=State.toggle_explore),

            ),
            rx.vstack(
                rx.cond(
                    State.explore_toggled,
                    explore_page(), library_page(),

                ),
                align = "top",
                height="100%",
            ),

            width="65%",
            height="100%",
            #bg_color = "#E1E8F0",
            bg_color = "red"

        ),

        rx.flex(
            rx.vstack(
                rx.image(
                    src="/logo.svg", width="100px", height="auto", margin_top="1em"
                ),
                create_new_chapp_sidebar(),
            ),
            width="35%",
            height="100%",
            box_shadow= "-4px 4px 15px 8px #C9D3DF",
        ),

    )

def create_new_chapp_sidebar():
    return rx.vstack(
        rx.text("What tools do you want to create", text_size="2em", padding ="5"),
        rx.vstack(
            rx.input(
                placeholder="Tool Description",
                on_change=ConfigChappState.set_description_of_chapp,
                id="tool_description",
                style = inp_style,
                margin_left = "1em",
                margin_right = "1em",

            ),
            rx.button("Submit", type_="confirm", on_click=ConfigChappState.create_chapp(), style = submit_style),
        ),

    )




def explore_page():
    return rx.vstack(
        rx.heading("Explore", font_size="2em", padding ="5"),
        rx.text("Explore Chapps other people have made"),
        rx.input(
            placeholder="Tool Description",
            id="tool_description",
            value=ExploreState.search_query,
            on_change=ExploreState.set_search_query,
            style = text_field,
        ),
        rx.button(
            "Submit", type_="submit", padding ="5",
            on_click=ExploreState.search_chaps
        ),
        chapp_grid(ExploreState.search_results),
    )

def library_page():
    return rx.vstack(
        rx.heading("Libary", font_size="2em", padding ="5"),
        chapp_grid(HomeState.my_chapps),
    )

def chapp_card(chapp: Chapp):
    return rx.box(
        rx.container(
            rx.image(src="/robo.jpg", width="100%", height="5em",border_top_left_radius= "30px", border_top_right_radius= "30px",),
            rx.link(
                rx.text(chapp.title, font_size="16px"),
                href=f"/chapp/{chapp.id}",
                padding_left="20px",
                padding_right="20px",
            ),center_content=True,

        ),
        height="8em", width="12em", bg="#EAF0F3",style = card_style,
    )

def chapp_grid(chapps: list[Chapp]) -> rx.Component:
    return rx.responsive_grid(
        rx.foreach(chapps, chapp_card),
        columns=[2, 3],
        spacing="20",
    )
