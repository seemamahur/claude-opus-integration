import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load API key from .env file
load_dotenv()

# Initialize Anthropic client
client = Anthropic()


# Make a simple request
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Say hello and tell me you are Claude, made by Anthropic."}
    ]
)

# Print the response
print("Claude says:")
print(message.content[0].text)




#start multi turn conversation 

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text


# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response
answer = chat(messages)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context
final_answer = chat(messages)

print_r(final_answer)

#end multi turn conversation




