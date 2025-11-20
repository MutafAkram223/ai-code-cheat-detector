# src/agents/nlp_feature_agent.py

import re

# AI-style comment patterns (humans rarely write these in CP)
AI_COMMENT_PHRASES = [
    "in this solution",
    "the idea is",
    "time complexity",
    "space complexity",
    "we start by",
    "the optimal approach",
    "first we",
    "next we",
    "finally we",
    "overall",
    "efficient solution",
]

# AI comment structure: Step-by-step explanation
AI_STEP_KEYWORDS = [
    "step 1", "step 2", "step 3",
    "first,", "second,", "third,"
]

def detect_comment_phrases(comment):
    c = comment.lower()
    return sum(1 for phrase in AI_COMMENT_PHRASES if phrase in c)

def detect_step_style(comment):
    c = comment.lower()
    return sum(1 for phrase in AI_STEP_KEYWORDS if phrase in c)

def detect_repetitive_ai_style(comment):
    """
    AI comments are repetitive and formal.
    Humans write short, rough comments.
    """
    words = re.findall(r"[a-zA-Z]+", comment.lower())
    if not words:
        return 0

    unique_ratio = len(set(words)) / len(words)

    # AI tends to have LOW unique ratios (repetition)
    if unique_ratio < 0.55:
        return 1
    return 0

def analyze_comments(code_text):
    comments = re.findall(r"//.*|/\*[\s\S]*?\*/", code_text)

    if not comments:
        return {"linguistic_score": 0.0}

    combined = " ".join(comments)

    phrase_hits = detect_comment_phrases(combined)
    step_hits = detect_step_style(combined)
    rep_score = detect_repetitive_ai_style(combined)

    # Weighted scoring — more strict for AI
    raw = (
        phrase_hits * 0.6 +
        step_hits * 0.5 +
        rep_score * 0.8
    )

    linguistic_score = min(raw / 4, 1.0)

    return {
        "linguistic_score": float(linguistic_score),
        "phrase_hits": phrase_hits,
        "step_hits": step_hits,
        "repetition_score": rep_score,
        "comments": comments
    }
