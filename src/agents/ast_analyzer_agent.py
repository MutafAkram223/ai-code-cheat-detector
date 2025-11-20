# src/agents/ast_analyzer_agent.py

import re

def detect_recursion(code):
    return 1 if re.search(r"\\bdfs\\b|\\brecurse\\b|\\bhelper\\b", code) else 0

def detect_bfs_dfs_templates(code):
    count = 0
    if "queue<" in code: count += 1
    if "stack<" in code: count += 1
    if "vector<vector" in code: count += 1
    return count

def detect_loop_style(code):
    """
    AI tends to write 'for (int i = 0; i < n; i++)'
    much more consistently than humans.
    """
    matches = re.findall(r"for\s*\(int\s+\w+\s*=\s*0;", code)
    return 1 if len(matches) >= 2 else 0

def analyze_structure(code):
    code = code or ""

    recur = detect_recursion(code)
    bfsdfs = detect_bfs_dfs_templates(code)
    loop_style = detect_loop_style(code)

    # Soft scoring (does not overpower behavioral)
    ast_score = min(
        recur * 0.4 +
        bfsdfs * 0.2 +
        loop_style * 0.4,
        1.0
    )

    return {
        "ast_score": float(ast_score),
        "recursion": recur,
        "bfsdfs": bfsdfs,
        "loop_style": loop_style
    }
