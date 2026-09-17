import streamlit as st
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

st.title("Chat with Claude")

user_input = st.text_input("Ask Claude something:")

if st.button("Send") and user_input:
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": user_input}]
    )
    st.write("**Claude says:**", message.content[0].text)
