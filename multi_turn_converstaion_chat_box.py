from helper_functions import *
from dotenv import load_dotenv
# from helper_functions import add_user_message, add_assistant_message, chat

# Load API key from .env file
load_dotenv()

# making a initial list of message
messages = []

# while True:     or #using while loop run chat bot forever
   #taking input  
   # one hit only, no loop
input_value = input("Say Something: ")
print(input_value)


# add user message into message
add_user_message(messages, input_value)

# call claude with the chat function 
answer = chat(
    messages,
    system="One word.",
    max_tokens=5,
    )

#add already generated text into messages

add_assistant_message(messages,answer)

print("Claude:", answer)
       


