"""
Problem parser: lightweight NLP that extracts keywords and attempts to classify expected algorithm categories.
Uses simple keyword heuristics + embeddings (optional).
"""
from sentence_transformers import SentenceTransformer
import re

MODEL = None
def _get_model():
    global MODEL
    if MODEL is None:
        MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    return MODEL

ALGO_KEYWORDS = {
    "two-sum": ["two sum", "two-sum", "two sum problem", "indices", "sum to target"],
    "hashmap": ["hash", "map", "unordered_map", "dictionary"],
    "two-pointer": ["two pointer", "two-pointer", "two pointers", "sorted", "left", "right"],
    "dp": ["dynamic programming", "dp", "memoization", "memo"],
    "graph": ["graph", "adjacency", "edges", "vertices", "bfs", "dfs"],
    "greedy": ["greedy", "choose", "maximize", "minimize", "greedy algorithm"],
    "binary-search": ["binary search", "sorted", "mid", "low", "high"],
}

def parse_problem(text):
    text_low = (text or "").lower()
    detected = []
    for name, kws in ALGO_KEYWORDS.items():
        for kw in kws:
            if kw in text_low:
                detected.append(name)
                break
    # Embedding representation optional
    model = _get_model()
    emb = model.encode(text or "", convert_to_numpy=True).tolist()
    return {
        "keywords_detected": detected,
        "problem_embedding": emb,
    }
