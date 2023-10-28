"""Base state for the app."""
import reflex as rx

class User(rx.Base):
    id: int
    name: str

class Example(rx.Base):
    inputs: list[str]
    output: str

class Chapp(rx.Base):
    id: int
    title: str
    short_description: str
    how_to_use: str
    icon_url: str
    inputs: list[str]
    examples: list[Example]
    instruction: list[str]

class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
    user: User
    logged_in: bool = False

    def create_user_or_login(self, name):
        self.logged_in = True
        pass

class HomeState(State):
    my_chapps = list[Chapp]

    def get_chaps(self):
        pass

class RunChappState(State):
    chapp: Chapp
    inputs: list[str]
    output: str
    status: str # waiting_for_user_response, running, finished

    def run_chapp(self):
        pass

class ExploreState(State):
    search_results = list[Chapp]

    def search_chaps(self, serach_query):
        pass

class ConfigState(State):
    chapp: Chapp
