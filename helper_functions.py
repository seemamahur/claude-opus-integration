from anthropic import Anthropic
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = Anthropic()   # reading ANTHROPIC_API_KEY from your environment
# model = "claude-opus-4-6"
model ="claude-haiku-4-5-20251001"   # cheapest Claude model for the testing

# Prices in dollars per 1 million tokens (Haiku 4.5)
INPUT_PRICE = 1.00
OUTPUT_PRICE = 5.00

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None, max_tokens=5):
    params = {    #Put the always-needed values in a dictionary
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
    }
    if system:
        params["system"] = system

    message = client.messages.create(**params)

    # The ** means "unpack the dictionary into named arguments". Python turns this: params = {"model": "claude-haiku-4-5-20251001", "max_tokens": 5, "messages": [...], "system": "One word."}

# or we can call like that easy way
#    def chat(messages, system, max_tokens=5):
#         message = client.messages.create(
#             model=model,
#             max_tokens=max_tokens,
#             messages=messages,
#             system=system,
#     )


    input_tokens = message.usage.input_tokens
    output_tokens = message.usage.output_tokens
    cost = (input_tokens * INPUT_PRICE + output_tokens * OUTPUT_PRICE) / 1_000_000

    print(f"[tokens] input: {input_tokens}, output: {output_tokens}")
    print(f"[cost] about ${cost:.6f}")

    return message.content[0].text