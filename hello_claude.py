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