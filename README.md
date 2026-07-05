# 🇩🇿 Assistant Aide à la Décision PME - Algérie

Un **chatbot intelligent basé sur RAG (Retrieval-Augmented Generation) et des Agents IA** pour accompagner les entrepreneurs et les PME algériennes dans leurs décisions stratégiques.

---

## 🚀 Fonctionnalités

- 📌 Réponses précises sur :
  - Création d'entreprise
  - Financement
  - Choix de la forme juridique
  - Business Plan
  - Gestion de trésorerie
  - Marketing
  - Fiscalité


- 🤖 Système multi-agents spécialisés
  - Juridique
  - Financement
  - Business Plan
  - Marketing
  - Gestion d'entreprise

- 🔎 Recherche documentaire avec RAG

- 💬 Interface web moderne développée avec Streamlit

- ⚡ Réponses rapides grâce à Groq

---

## 🛠️ Technologies utilisées

- LangChain
- LangGraph
- Groq (Llama-3.3-70B)
- HuggingFace Embeddings
- ChromaDB
- Streamlit
- Python

---

## 📂 Structure du projet

```text

## Structure du projet
aide-decision-pme/
├── data/                    # Documents sources (Markdown)
├── src/
    ├── agents.py 
│   ├── config.py
│   └── rag_chain.py
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md


```

---

# ⚙️ Installation

## 1. Cloner le dépôt

```bash
git clone git clone https://github.com/ayaaouimeur/aide-decision-pme.git
cd aide-decision-pme
```

---

## 2. Créer un environnement virtuel

### Windows

```bash
python -m venv rag_env
rag_env\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv rag_env
source rag_env/bin/activate
```

---

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 4. Configurer les variables d'environnement

Créer un fichier `.env` à la racine du projet.

```env
GROQ_API_KEY=ta_cle_groq
```

---

## 5. Lancer l'application

```bash
streamlit run streamlit_app.py
```

L'application sera accessible à l'adresse suivante :

```
https://aide-decision-pme-6t3ova3nrf9jwn8wvvfcph.streamlit.app
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

