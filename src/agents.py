# src/agents.py
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.rag_chain import DecisionAidRAG
from src.config import *

class Agent:
    def __init__(self, name, system_prompt):
        self.name = name
        self.llm = ChatGroq(model=LLM_MODEL, temperature=0.3, api_key=GROQ_API_KEY)
        self.prompt = ChatPromptTemplate.from_template(system_prompt + "\n\nHistorique de conversation : {history}\n\nQuestion : {question}\nRéponse :")

    def invoke(self, question, history=""):
        chain = self.prompt | self.llm | StrOutputParser()
        return chain.invoke({"question": question, "history": history})

class Coordinator:
    def __init__(self):
        self.rag = DecisionAidRAG()
        self.juridique_agent = Agent("Juridique", "Tu es expert en formes juridiques et création d'entreprise en Algérie.")
        self.financement_agent = Agent("Financement", "Tu es expert en financement ANSEJ, ANDI et banques en Algérie.")
        self.business_plan_agent = Agent("Business Plan", "Tu es expert en rédaction de business plan pour PME en Algérie.")

    def process(self, question, history=""):
        question_lower = question.lower()
        if "forme juridique" in question_lower or "sarl" in question_lower or "eurl" in question_lower or "pharmaceutique" in question_lower:
            return self.juridique_agent.invoke(question, history)
        elif "ansej" in question_lower or "financement" in question_lower:
            return self.financement_agent.invoke(question, history)
        elif "business plan" in question_lower:
            return self.business_plan_agent.invoke(question, history)
        else:
            return self.rag.ask(question)