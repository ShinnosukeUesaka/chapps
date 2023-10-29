import reflex as rx
@rx.page(route="/loading", title="Home")
def loading_page():
    return rx.box(
        rx.progress(is_indeterminate=True, width="100%", position='absolute', z_value=1),
        rx.image(src='/loading_page_bg.png', width='auto', height='1080', z_value=0),
        background_color = '#EAF0F3',
    )
