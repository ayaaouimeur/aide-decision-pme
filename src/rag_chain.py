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
        print("🚀 Initialisation du RAG...\n")

        loader = DirectoryLoader(DATA_PATH, glob="**/*.txt", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
        chunks = text_splitter.split_documents(docs)
        print(f"✅ {len(chunks)} chunks créés.")

        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=CHROMA_PATH)

        retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

        llm = ChatGroq(model=LLM_MODEL, temperature=0.25, api_key=GROQ_API_KEY)

        # Prompt très strict et professionnel
        system_template = """
        Tu es un consultant senior en création et gestion de PME en Algérie.
        Réponds de manière claire, concise et structurée.
        Utilise uniquement les informations du contexte.
        Structure tes réponses avec des titres et puces quand c'est utile.
        Sois direct et professionnel. Évite les phrases inutiles et les répétitions.
        """

        prompt = ChatPromptTemplate.from_template("""
        Contexte :
        {context}

        Question : {question}

        Réponse concise et structurée :
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
        print(response)
        print("\n" + "-"*80 + "\n")
        return response