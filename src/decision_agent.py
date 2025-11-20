"""
Generate final human-readable explanation & mapping from scores -> verdict.
"""
def explain_decision(result_obj, all_scores):
    # result_obj contains verdict & confidence & raw_score
    verdict = result_obj.get("verdict", "Uncertain")
    conf = result_obj.get("confidence", 0.0)
    raw = result_obj.get("raw_score", 0.0)
    explanation_lines = []
    explanation_lines.append(f"**Final verdict:** **{verdict}** (confidence {conf*100:.1f}%).\n")
    explanation_lines.append("**Signal contributions:**")
    for k, v in all_scores.items():
        explanation_lines.append(f"- **{k}**: {v:.4f}")
    explanation_lines.append("\n**Why this verdict?**")
    if verdict.lower().find("ai") != -1:
        explanation_lines.append("- High similarity to AI sample(s) and/or suspicious behavioral signals.")
    elif verdict.lower().find("human") != -1:
        explanation_lines.append("- Low similarity to AI samples, human-like behavior and varied code structure.")
    else:
        explanation_lines.append("- Signals are mixed or uncertain; manual review recommended.")
    return "\n\n".join(explanation_lines)
