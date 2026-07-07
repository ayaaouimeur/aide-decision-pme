# streamlit_app.py
import streamlit as st
from src.agents import Coordinator
from langgraph.checkpoint.memory import MemorySaver

st.set_page_config(page_title="Assistant Aide à la Décision PME", layout="centered")
st.title("🤖 Assistant Aide à la Décision PME - Algérie")
st.markdown("**Consultant IA pour entrepreneurs algériens**")

# Initialisation avec mémoire persistante
if "coordinator" not in st.session_state:
    with st.spinner("Initialisation des agents..."):
        st.session_state.coordinator = Coordinator()
        st.session_state.checkpointer = MemorySaver()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Posez votre question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Réflexion en cours..."):
            response = st.session_state.coordinator.process(prompt, history="\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-6:]]))
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

st.caption("Portfolio AI Engineer - Aouimeur Aya")