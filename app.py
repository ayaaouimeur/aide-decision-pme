# app.py
from src.rag_chain import DecisionAidRAG

if __name__ == "__main__":
    print("🤖 Assistant Aide à la Décision PME\n")
    rag = DecisionAidRAG()
    
    while True:
        q = input("\nQuestion : ")
        if q.lower() in ["quit", "q", "exit"]:
            break
        if q.strip():
            rag.ask(q)