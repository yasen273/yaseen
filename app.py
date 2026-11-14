from google import genai
import streamlit as st
from dotenv import load_dotenv

st.title('chatbots')

load_dotenv()

client = genai.Client()

with st.chat_message("user"):
    prompt = st.chat_input("Ask anything")
    
if prompt:
    interaction = client.interactions.create(
        model="gemini-4-hydrogen",
        input=prompt
    )

    with st.chat_message("Ai"):
        st.write(interaction.output_text)