# streamlit_app.py
import streamlit as st
from src.rag_chain import DecisionAidRAG

# Configuration de la page
st.set_page_config(
    page_title="Aide Décision PME | Algérie",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Thème moderne bleu foncé
st.markdown("""
    <style>
    .stApp {
        background-color: #0F172A;
        color: #E2E8F0;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 12px;
    }
    .stChatMessage.user {
        background-color: #1E40AF;
    }
    .stChatMessage.assistant {
        background-color: #1E2937;
    }
    h1, h2, h3 {
        color: #60A5FA;
    }
    .stButton>button {
        background-color: #3B82F6;
        color: white;
        border-radius: 10px;
        height: 45px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🚀 Aide Décision PME")
    st.markdown("**Consultant IA pour entrepreneurs algériens**")
    st.markdown("---")
    
    st.markdown("### 📌 Thèmes disponibles")
    st.markdown("• Création d'entreprise")
    st.markdown("• Formes juridiques (EURL, SARL, SAS)")
    st.markdown("• Business Plan")
    st.markdown("• Financement (ANSEJ, ANDI, Banques)")
    st.markdown("• Trésorerie & Gestion")
    st.markdown("• Marketing & Stratégie")
    
    st.markdown("---")
    if st.button("🗑️ Nouvelle Conversation"):
        st.session_state.messages = []
        st.rerun()

# Header principal
col1, col2 = st.columns([1, 6])
with col1:
    st.markdown("# 🤖")
with col2:
    st.title("Assistant Aide à la Décision")
    st.markdown("**Votre consultant virtuel pour les PME en Algérie**")

# Initialisation du RAG
if "rag" not in st.session_state:
    with st.spinner("Chargement du système intelligent..."):
        st.session_state.rag = DecisionAidRAG()

# Historique du chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Zone de saisie
if prompt := st.chat_input("Posez votre question ici..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Réflexion en cours..."):
            response = st.session_state.rag.ask(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.caption("💼 Projet Portfolio - AI Engineer | Développé en 2026 Par Aouimeur Aya")