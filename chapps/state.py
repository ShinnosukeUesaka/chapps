"""Base state for the app."""
import reflex as rx
from chapps import firebase_utils
import yaml
from chapps.openai_utils import create_chat_and_parse, GPTConfig, create_chat
from chapps.firebase_utils import db
import uuid
from typing import Optional

class User(rx.Base):
    id: str
    name: str


class Example(rx.Base):
    inputs: dict[str, str]
    output: str

class Input(rx.Base):
    name: str
    description: str

class Chapp(rx.Base):
    id: str
    user: str
    title: str
    short_description: str
    description: str
    icon_url: str = None
    inputs: list[Input]
    examples: list[Example]
    instruction: str


class State(rx.State):
#class State:
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """

    user: User = User(id="", name="")
    logged_in: bool = False
    explore_toggled: bool = False

    def check_logged_in(self):
        if not self.logged_in:
            return rx.redirect("/login")

    def toggle_explore(self):
        self.explore_toggled = not self.explore_toggled

    def set_username(self, username):
        self.user.name = username

    def create_user_or_login(self):
        user_data = firebase_utils.add_or_get_user(self.user.name)
        self.user = User(id=user_data["id"], name=user_data["name"])
        self.logged_in = True


class HomeState(State):
    my_chapps: list[Chapp]

    def get_chapps(self):
        self.my_chapps = []
        data = db.collection("chapps").where("user", "==", self.user.id).stream()
        for doc in data:
            chapp = doc.to_dict()
            self.my_chapps.append(Chapp(**chapp))

class RunChappState(State):
    chapp: Chapp = None
    inputs: dict[str, str] = {}
    output: str
    status: str

    def get_chapp(self):
        chapp_id = self.get_query_params()["chapp_id"]
        print(chapp_id)
        doc = db.collection("chapps").document(chapp_id).get()
        chapp = doc.to_dict()
        self.chapp = Chapp(**chapp)

    def set_input(self, name, value):
        self.inputs[name] = value

    def run_chapp(self):
        self.output = call_chapp(self.chapp, self.inputs)


class ConfigChappState(State):
    unsaved_chapp: Optional[Chapp] = None
    generating_chapp: bool = False
    description_of_chapp: str = None

    def edit_chapp(self, chapp_id):
        doc = db.collection("chapps").document(chapp_id).get()
        chapp = doc.to_dict()
        self.generating_chapp = False
        self.unsaved_chapp = Chapp(**chapp)
        return rx.redirect("/chappConfig")

    def create_chapp(self):
        self.generating_chapp = True
        yield
        chapp = create_chapp(self.description_of_chapp, self.user.id)
        self.unsaved_chapp = chapp
        self.generating_chapp = False
        return rx.redirect("/chappConfig")

    def save_chapp(self):
        db.collection("chapps").document(self.unsaved_chapp.id).set(self.unsaved_chapp.dict())
        return rx.redirect("/")

    def edit_title(self, text):
        self.unsaved_chapp.title = text

    def edit_short_description(self, text):
        self.unsaved_chapp.short_description = text

    def edit_description(self, text):
        self.unsaved_chapp.description = text

    def edit_icon_url(self, text):
        self.unsaved_chapp.icon_url = text

    def edit_instruction(self, text):
        self.unsaved_chapp.instruction = text

    def edit_input_description(self, description, name):
        for input in self.unsaved_chapp.inputs:
            if input.name == name:
                input.description = description

    def edit_input_name(self, name, description):
        for input in self.unsaved_chapp.inputs:
            if input.description == description:
                input.name = name

    def add_input(self):
        self.unsaved_chapp.inputs.append(Input(name="", description=""))

    def delete_input(self, name):
        for input in self.unsaved_chapp.inputs:
            if input.name == name:
                self.unsaved_chapp.inputs.remove(input)

    def edit_examples(self):

        pass

class ExploreState(State):
    search_query: str = ''
    search_results: list[Chapp] = []

    def search_chaps(self):
        self.search_results = []
        query = self.search_query
        #TODO semantic search
        # for now random search with limit of 5.
        data = db.collection("chapps").limit(5).stream()
        for doc in data:
            chapp = doc.to_dict()
            self.search_results.append(Chapp(**chapp))









def create_chapp(description: str, user_id: str) -> Chapp:
    prompt = """
Your job is to create a Chapp based on the prompt below. Chapp is a tool or an app that runs on GPT-4.

Give me the all the variables neccesary to define the chapp.
A chapp has a title, description, short description inputs variables(all lowercase and use underscore for multiple words), instruction(prompt for gpt-4), example pair of inputs and outputs. All the input variables are string.
The output must strictly follow the example yaml format below, as it would be parsed programatically.


Example Input
I want a tool that gives me a definition of a word, and three example sentences based on a context provided.

Example Output

title: Word Context Definition and Example Builder

short_description: A tool for learning new words and their usage in a specific context.

description: |-
   This Chapp provides you the definition of a specific word and constructs three sentences using that word, based around a specific context provided by the user. It's a tool that can be handy for learning new words, enhancing your vocabulary, and understanding the usage of a word in a context effectively.

inputs:
  - name: word
    description: Enter the word you want to learn about and see used in sentences.
  - name: context
    description: Specify the context or theme within which you want to see the word used.
instruction: |-
  For the word "{word}", first provide a clear and concise definition. Then, based on the context of "{context}", create three unique sentences that correctly use and demonstrate the meaning of the word.

example:
  inputs:
    word: procrastinate
    context: school
  output: |-
    ## Definition
    Procrastinate means to delay or postpone action; put off doing something.
    ## Example Sentences:
    1. Many students tend to procrastinate when it comes to studying for exams, often leading to stress and poor performance.
    2. In school, procrastinating on assignments can result in late submissions and penalties.
    3. Despite knowing the importance of timely work, John often found himself procrastinating on his school projects.
"""

    def parsing_function(yaml_str: str) -> Chapp:
        chapp_data = yaml.safe_load(yaml_str)
        print(chapp_data)
        uid = uuid.uuid4().hex
        chapp_data["examples"] = [chapp_data["example"]]
        chapp_data["id"] = uid
        chapp_data["user"] = user_id
        return Chapp(**chapp_data)

    messages = [
        {"role": "user", "content": prompt},
        {"role": "user", "content": description},
    ]
    chapp = create_chat_and_parse(
        messages=messages, parsing_function=parsing_function, gpt_config=GPTConfig()
    )

    return chapp


def call_chapp(chapp: Chapp, inputs: dict[str, str]) -> str:
    formated_instruction = chapp.instruction.format(**inputs)
    example_string = "Example Input\n"
    for example in chapp.examples:
        for key, value in example.inputs.items():
            example_string += f"{key}: {value}\n"
        example_string += f"\nExample Output\n{example.output}"


    prompt = f"""{formated_instruction}
Strictly follow the format of the example below.

{example_string}
"""

    return create_chat(messages=[{"role": "user", "content": prompt}], gpt_config=GPTConfig())
