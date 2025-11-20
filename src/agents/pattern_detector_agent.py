# src/agents/pattern_detector_agent.py

import re

# AI-style variable names (very consistent, humans mix styles)
AI_NAME_PATTERNS = [
    r"\btemp\b", r"\bcurr\b", r"\bprev\b", r"\bans\b", r"\bres\b",
    r"\bidx\b", r"\bid\b", r"\bpos\b", r"\bptr\b"
]

# AI-style helper function names
AI_FUNCTION_PATTERNS = [
    r"\bsolve\b", r"\bdfs\b", r"\bbfs\b", r"\bhelper\b",
    r"\bcompute\b", r"\bprocess\b"
]

# AI algorithm templates
AI_TEMPLATE_SNIPPETS = [
    r"sort\(.*\.begin",
    r"vector<vector<",
    r"unordered_map<",
    r"priority_queue<",
    r"while\s*\(\s*!q\.empty",
]

# AI-style loop patterns (human loops vary a lot)
AI_LOOP_TEMPLATES = [
    r"for\s*\(\s*int\s+\w+\s*=\s*0\s*;\s*\w+\s*<\s*\w+\s*;\s*\w+\+\+\)",
    r"for\s*\(\s*auto\s*&",
]

def count_matches(patterns, code):
    total = 0
    for p in patterns:
        matches = re.findall(p, code)
        total += len(matches)
    return total

def detect_patterns(code_text):
    code = code_text or ""

    name_hits = count_matches(AI_NAME_PATTERNS, code)
    fn_hits = count_matches(AI_FUNCTION_PATTERNS, code)
    template_hits = count_matches(AI_TEMPLATE_SNIPPETS, code)
    loop_hits = count_matches(AI_LOOP_TEMPLATES, code)

    # Weighted scoring — stronger than before
    raw = (
        name_hits * 0.4 +
        fn_hits * 0.6 +
        template_hits * 0.8 +
        loop_hits * 0.6
    )

    # Hard cap for normalization (CP code is short)
    pattern_score = min(raw / 6, 1.0)

    return {
        "pattern_score": float(pattern_score),
        "name_hits": name_hits,
        "func_hits": fn_hits,
        "template_hits": template_hits,
        "loop_hits": loop_hits
    }
