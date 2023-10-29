"""Base state for the app."""
import reflex as rx
from chapps import firebase_utils


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
    user: User = None
    logged_in: bool = False

    def create_user_or_login(self, name):
        user_data = firebase_utils.add_or_get_user(name)
        self.user.id = user_data['id']
        self.user.name = user_data['name']

        self.logged_in = True
        pass

class HomeState(State):
    my_chapps: list[Chapp]

    def get_chaps(self):
        pass

class RunChappState(State):
    chapp: Chapp = None
    inputs: list[str]
    output: str
    status: str # waiting_for_user_response, running, finished

    def run_chapp(self):
        pass

class CreateNewState(State):
    description_of_chapp: str = None

class ExploreState(State):
    search_query: str = None
    search_results: list[Chapp] = []

    def search_chaps(self):
        self.search_results.append(Chapp(
                id=1,
                title="test",
                short_description="dsf",
                how_to_use="sd",
                icon_url="fd",
                inputs=[],
                examples=[],
                instruction=[],
            )
        )



class ConfigState(State):
    chapp: Chapp = Chapp(
        id=1,
        title="test",
        short_description="shitty crappy chatGPT UX improvement",
        how_to_use="sd",
        icon_url="fd",
        inputs=[],
        examples=[],
        instruction=[],
    )
    def change_short_description(self, short_description):
        self.chapp.short_description = short_description
    def change_how_to_use(self, how_to_use):
        self.chapp.how_to_use = how_to_use
    def change_icon_url(self, icon_url):
        self.chapp.icon_url = icon_url
    def change_inputs(self, inputs):
        self.chapp.inputs = inputs.append(inputs)
    # def change_examples(self, examples):

