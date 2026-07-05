# src/rag_chain.py - Version Stable et Professionnelle
from langchain_groq import ChatGroq
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.config import *

class DecisionAidRAG:
    def __init__(self):
        self.rag_chain = None
        self.initialize()

    def initialize(self):
        print("🚀 Initialisation du RAG Professionnel...\n")

        # Chargement des documents
        loader = DirectoryLoader(DATA_PATH, glob="**/*.md", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
        docs = loader.load()
        print(f"📄 {len(docs)} documents chargés.")

        # Chunking Amélioré + Metadata
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=700,
            chunk_overlap=150,
            separators=["\n\n", "\n", ".", "!", "?", " ", ""]
        )
        chunks = text_splitter.split_documents(docs)
        print(f"✅ {len(chunks)} chunks créés.")
        
        # Ajout de metadata pour chaque chunk
        for chunk in chunks:
            if 'source' not in chunk.metadata:
                chunk.metadata['source'] = 'Document inconnu'        

        # Embeddings Améliorés
        embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")

        # Vector Store
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=CHROMA_PATH
        )

        retriever = vectorstore.as_retriever(search_kwargs={"k": 6})

        # LLM
        llm = ChatGroq(model=LLM_MODEL, temperature=0.25, api_key=GROQ_API_KEY)

        # Prompt Professionnel
        system_template = """
        Tu es un consultant senior très expérimenté en création et gestion de PME en Algérie.
        Tu accompagnes des entrepreneurs avec un ton professionnel, clair, encourageant mais réaliste.

        Règles à respecter :
        - Réponds uniquement avec les informations du contexte fourni.
        - Si tu n'as pas assez d'informations, dis : "Selon les documents dont je dispose, je n'ai pas d'information détaillée sur ce point."
        - Structure tes réponses avec des titres et puces.
        - Sois concret et actionnable.
        - Parle de façon naturelle.
        """

        prompt = ChatPromptTemplate.from_template("""
        Contexte :
        {context}

        Question : {question}

        Réponse :
        """)

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        # Chaîne RAG finale
        self.rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        print("✅ RAG Professionnel initialisé !\n")

    def ask(self, question: str):
        response = self.rag_chain.invoke(question)
        return response