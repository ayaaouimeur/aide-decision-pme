# Assistant Aide à la Décision PME - Algérie

Un chatbot intelligent basé sur RAG pour aider les entrepreneurs et PME en Algérie.

---

## Technologies utilisées
- LangChain
- Groq (Llama-3.3-70B)
- HuggingFace Embeddings
- Chroma
- Streamlit

---

## Structure du projet
aide-decision-pme/
├── data/                    # Documents sources (Markdown)
├── src/
│   ├── config.py
│   └── rag_chain.py
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
text---

## Installation Locale

1. Cloner le repository
```bash
git clone https://github.com/ayaaouimeur/aide-decision-pme.git
cd aide-decision-pme

Créer l'environnement virtuel

Bashpython -m venv rag_env
rag_env\Scripts\activate      # Windows

Installer les packages

Bashpip install -r requirements.txt

Ajouter ta clé Groq
Crée un fichier .env à la racine et mets :

envGROQ_API_KEY=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

Lancer l'application

Bashstreamlit run streamlit_app.py

Fonctionnalités

Réponses sur création d'entreprise, financement ANSEJ/ANDI, formes juridiques, business plan, trésorerie, marketing...
Interface web avec Streamlit
Sources citées


Développé par Aouimeur Aya
Projet Portfolio AI Engineer - Juin 2026