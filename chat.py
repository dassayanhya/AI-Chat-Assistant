import streamlit as st
import google.generativeai as genai
from streamlit_chat import message

# Set up Google Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

if "gemini_model" not in st.session_state:
    st.session_state["gemini_model"] = "gemini-2.0-flash-lite"  # Ensure correct model name

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Define system instruction
system_instruction = " PUT YOUR SYSTEAM INSTRUCTION HERE !!! "

# User input
prompt = st.chat_input("Ask me anything!")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    full_response = ""

    try:
        model = genai.GenerativeModel(st.session_state["gemini_model"])

        # Combine system instructions + prompt
        full_prompt = f"{system_instruction}\n\nUser: {prompt}"

        response_stream = model.generate_content(full_prompt, stream=True)

        with st.chat_message("assistant"):
            response_container = st.empty()
            for chunk in response_stream:
                full_response += chunk.text
                response_container.markdown(full_response)

    except Exception as e:
        full_response = f"An error occurred: {e}"

    st.session_state.messages.append({"role": "assistant", "content": full_response})
