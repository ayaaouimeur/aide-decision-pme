# src/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Charge les variables d'environnement si on crée un .env plus tard

# ==================== CONFIGURATION GÉNÉRALE ====================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("⚠️  ATTENTION : GROQ_API_KEY non trouvée dans le fichier .env")
    
# Paramètres du RAG
CHUNK_SIZE = 700
CHUNK_OVERLAP = 120
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"   # Bon rapport qualité/vitesse
LLM_MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.35
TOP_K = 5   # Nombre de documents à récupérer

# Chemins
DATA_PATH = "data"
CHROMA_PATH = "chroma_db"