"""Styles for the app."""

import reflex as rx

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"
border = "1px solid #F4F3F6"
text_color = "black"
accent_text_color = "#1A1060"
accent_color = "#F5EFFE"
hover_accent_color = {"_hover": {"color": accent_color}}
hover_accent_bg = {"_hover": {"bg": accent_color}}
content_width_vw = "90vw"
sidebar_width = "20em"

template_page_style = {"padding_top": "5em", "padding_x": ["auto", "2em"]}

template_content_style = {
    "width": "100%",
    "align_items": "flex-start",
    "box_shadow": box_shadow,
    "border_radius": border_radius,
    "padding": "1em",
    "margin_bottom": "2em",
}

link_style = {
    "color": text_color,
    "text_decoration": "none",
    **hover_accent_color,
}

overlapping_button_style = {
    "background_color": "white",
    "border": border,
    "border_radius": border_radius,
}

base_style = {
    rx.MenuButton: {
        "width": "3em",
        "height": "3em",
        **overlapping_button_style,
    },
    rx.MenuItem: hover_accent_bg,
      
}

markdown_style = {
    "code": lambda text: rx.code(text, color="#1F1944", bg="#EAE4FD"),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        font_weight="bold",
        color="#03030B",
        text_decoration="underline",
        text_decoration_color="#AD9BF8",
        _hover={
            "color": "#AD9BF8",
            "text_decoration": "underline",
            "text_decoration_color": "#03030B",
        },
    ),
}

header_style = {
    "text-align": "center",
    "font-size": "4rem",
    "font-weight": "600",
}

inp_style = {
    "border-radius": "1.875rem",
    "background": "#EAF0F3",
    "box-shadow": "-4px -4px 8px 4px #FFF, 4px 4px 8px 4px #D9D9D9",
    "width": "32.1875em",
    "margin-bottom": "50px"
}

submit_style = {
    "width": "10.375rem",
    "height": "2.5625rem",
    "flex-shrink": "0",
    "text_color" : "white",
    "border-radius": "2.5rem",
    "margin-block-start": "-200px",
    "background": "linear-gradient(93deg, #0068AB 5.3%, #00BDD3 70.88%, #4AF1FD 136.46%)",
}

card_style = {
    "border-radius": "30px",
    "background": "#E1E8F0",
    "box-shadow": "-4px -4px 8px 4px #FFF, 4px 4px 8px 4px #D9D9D9"
}

button_style = {
    "height": "2.5625rem",
    "flex-shrink": "0",
    "text_color" : "white",
    "border-radius": "2.5rem",
    "background": "linear-gradient(93deg, #0068AB 5.3%, #00BDD3 70.88%, #4AF1FD 136.46%)",
}