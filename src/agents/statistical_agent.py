"""
Statistical metrics: use lizard for cyclomatic complexity and tokens,
and compute entropy and identifier diversity heuristics.
"""
import lizard
import re
import math
from collections import Counter

def shannon_entropy(s):
    if not s:
        return 0.0
    freq = Counter(s)
    total = len(s)
    ent = 0.0
    for _, v in freq.items():
        p = v/total
        ent -= p * math.log2(p)
    return ent

def compute_statistical_scores(code_text):
    s = code_text or ""
    try:
        analysis = lizard.analyze_file.analyze_source_code("solution.cpp", s)
        # lizard returns a FileInformation object with functions list
        total_cc = sum([func.cyclomatic_complexity for func in analysis.function_list]) if analysis.function_list else 0
        average_cc = total_cc / max(1, len(analysis.function_list))
    except Exception:
        average_cc = 0.0
    # identifier diversity: count variable-like tokens
    tokens = re.findall(r'\b[A-Za-z_][A-Za-z0-9_]{1,30}\b', s)
    if len(tokens) == 0:
        id_div = 0.0
    else:
        id_div = len(set(tokens)) / len(tokens)
    ent = shannon_entropy(s)
    # crude stat score: normalize metrics into [0,1] where large anomaly -> closer to 1
    # use heuristics: very low id_div (<0.2) or very low cc -> suspicious
    stat_raw = (ent * 0.5) + (id_div * 0.5)
    stat_score = 1.0 / (1.0 + math.exp(- (stat_raw - 0.3)))
    return {
        "average_cyclomatic_complexity": average_cc,
        "identifier_diversity": id_div,
        "entropy": ent,
        "stat_score": float(stat_score)
    }
