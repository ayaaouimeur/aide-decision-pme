# Assistant Aide à la Décision PME - Algérie

**Un chatbot intelligent basé sur RAG + Agents** pour aider les entrepreneurs et les PME en Algérie à prendre de meilleures décisions.

---

# 🚀 Présentation

Cet outil est un assistant IA spécialisé dans le contexte algérien. Il répond aux questions sur :

- Création d’entreprise
- Formes juridiques (SARL, EURL, SAS...)
- Financement (ANSEJ, ANDI, CNAC...)
- Business Plan
- Gestion de trésorerie
- Marketing et stratégie

## Fonctionnalités principales

- RAG avec documents structurés
- Système d’agents spécialisés (Juridique, Financement, Business Plan...)
- Mémoire de conversation
- Interface web moderne

---

# 🛠️ Technologies

- **LangChain + LangGraph** : Orchestration RAG et Agents
- **Groq (Llama-3.3-70B)** : Modèle principal
- **HuggingFace Embeddings** : Recherche sémantique
- **Chroma** : Base vectorielle
- **Streamlit** : Interface utilisateur

---

# 📁 Structure du Projet

```text
aide-decision-pme/
├── data/                    # Documents sources (Markdown)
├── src/
│   ├── config.py
│   ├── rag_chain.py
│   └── agents.py
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
```


---

# 📚 Base de connaissances

Le chatbot utilise une base documentaire contenant notamment :

- Création d'entreprise en Algérie
- Financement des PME
- Fiscalité
- Comptabilité
- Marketing
- Business Plan
- Transformation digitale





---

# 🤖 Architecture

```text
Utilisateur
      │
      ▼
 Interface Streamlit
      │
      ▼
 LangGraph (Agents)
      │
      ▼
 Agent spécialisé
      │
      ▼
 RAG
      │
      ▼
 ChromaDB
      │
      ▼
 Embeddings
      │
      ▼
 Llama 3.3 70B (Groq)
```



---

# 🛠️ Installation Locale

## 1. Cloner le repository

```bash
git clone https://github.com/ayaaouimeur/aide-decision-pme.git
cd aide-decision-pme
```

## 2. Créer l'environnement virtuel

```bash
python -m venv rag_env
```

### Activer l'environnement (Windows)

```bash
rag_env\Scripts\activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

## 4. Ajouter ta clé Groq

Créer un fichier `.env` :

```env
GROQ_API_KEY=ta_clé_groq_ici
```

## 5. Lancer l'application

```bash
streamlit run streamlit_app.py
```

L'application sera accessible à l'adresse suivante :

```
https://aide-decision-pme-6t3ova3nrf9jwn8wvvfcph.streamlit.app
```
