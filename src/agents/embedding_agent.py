from sentence_transformers import SentenceTransformer
import os
import numpy as np
from src.utils.similarity_utils import cosine_sim

MODEL = None
def _get_model():
    global MODEL
    if MODEL is None:
        MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    return MODEL

def _load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def compute_embedding_scores(user_code_text, ai_sample_paths):
    model = _get_model()
    user_emb = model.encode(user_code_text or "", convert_to_numpy=True)
    sims = []
    for p in ai_sample_paths:
        try:
            sample_text = _load_text(p)
            sample_emb = model.encode(sample_text or "", convert_to_numpy=True)
            sims.append(float(cosine_sim(user_emb, sample_emb)))
        except Exception:
            sims.append(0.0)
    if len(sims) == 0:
        avg_sim = 0.0
    else:
        avg_sim = float(np.mean(sims))
    return {"similarity_score": avg_sim, "per_sample": sims}
