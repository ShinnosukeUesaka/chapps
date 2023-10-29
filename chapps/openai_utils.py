from dataclasses import dataclass
import openai
from typing import Callable

@dataclass
class GPTConfig():
  model: str = "gpt-4"
  temperature: float = 0
  max_tokens: int = 3096
  top_p: float = 1
  presence_penalty: float = 0
  frequency_penalty: float = 0


def create_chat(messages,
                gpt_config: GPTConfig = GPTConfig(),
                clean_output = True):
    print("------------------------------------")
    print(messages)
    print("------------------------------------")

    result = openai.ChatCompletion.create(
      messages=messages,
      model=gpt_config.model,
      top_p=gpt_config.top_p,
      presence_penalty=gpt_config.presence_penalty,
      frequency_penalty=gpt_config.frequency_penalty,
      max_tokens=gpt_config.max_tokens,
      temperature=gpt_config.temperature
    )
    print(result['choices'][0].message.content)
    if clean_output:
      return result['choices'][0].message.content.strip()
    else:
      return result['choices'][0].message.content

class ParsingError(Exception):
    pass

def generate_and_parse(gpt_function: Callable[[GPTConfig], str], parsing_function: Callable[[str], any], gpt_config, max_tries=2):
    # run gpt function until parsable.
    for i in range(max_tries):
        output = gpt_function(gpt_config)
        try:
            parsed_output = parsing_function(output)
            break
        except:
            if gpt_config.temperature < 0.3:
                gpt_config.temperature += 0.1
            pass
    else:
        raise ParsingError(f"Failed to parse output. GPT output: \n{output}")

    return parsed_output

def create_chat_and_parse(messages, parsing_function: Callable, gpt_config: GPTConfig = GPTConfig(), clean_output = True, max_tries=2):
    return generate_and_parse(gpt_function=lambda gpt_config: create_chat(messages, gpt_config, clean_output),
                       parsing_function=parsing_function,
                       gpt_config=gpt_config,
                       max_tries=max_tries)
