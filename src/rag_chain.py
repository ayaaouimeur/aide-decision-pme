# src/rag_chain.py
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
        print("🚀 Initialisation du RAG Avancé...\n")

        loader = DirectoryLoader(DATA_PATH, glob="**/*.md", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
        docs = loader.load()
        print(f"📄 {len(docs)} documents chargés.")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=650,
            chunk_overlap=130
        )
        chunks = text_splitter.split_documents(docs)
        print(f"✅ {len(chunks)} chunks créés.")

        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=CHROMA_PATH
        )

        retriever = vectorstore.as_retriever(search_kwargs={"k": 6})

        llm = ChatGroq(model=LLM_MODEL, temperature=0.25, api_key=GROQ_API_KEY)

        # Prompt amélioré pour des réponses naturelles et précises
        system_template = """
        Tu es un consultant senior très expérimenté en création et gestion de PME en Algérie.
        Tu parles de façon naturelle, directe et professionnelle, comme si tu accompagnais un entrepreneur motivé.

        Règles importantes :
        - Réponds uniquement avec les informations présentes dans le contexte.
        - Si le contexte ne suffit pas, dis clairement : "Selon les documents dont je dispose, je n'ai pas d'information détaillée sur ce point."
        - Sois concret et actionnable.
        - Structure tes réponses (titres + puces) pour qu'elles soient faciles à lire.
        - Évite les répétitions et les phrases inutiles.
        """

        prompt = ChatPromptTemplate.from_template("""
        Contexte :
        {context}

        Question : {question}

        Réponse :
        """)

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        self.rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        print("✅ RAG prêt !\n")

    def ask(self, question: str):
        print(f"❓ Question : {question}\n")
        response = self.rag_chain.invoke(question)
        print("📌 Réponse :\n")
        print(response)
        print("\n" + "="*85 + "\n")
        return response