"""Welcome to Reflex!."""

from chapps import styles

# Import all the pages.
from chapps.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
