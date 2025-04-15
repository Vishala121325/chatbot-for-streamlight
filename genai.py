import streamlit as st 
import google.generativeai as genai

genai.configure(api_key="AIzaSyAwDN9UO-6nu4eOQ0WIa4mK8hLnjMl41CU")

model = genai.GenerativeModel('gemini-1.5-flash')  # Or use 'gemini-pro'

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Gemini AI Chatbot")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask something...")
if user_input:
  
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = st.session_state.chat.send_message(user_input)
        answer = response.text
    except Exception as e:
        answer = f"⚠️ Error: {str(e)}"

    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
