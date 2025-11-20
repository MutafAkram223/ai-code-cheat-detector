# src/classifiers/ensemble_classifier.py

def compute_final_decision(scores):
    """
    Ensemble classifier with strong behavioral dominance.
    Optimized for competitive programming cheating detection.
    """

    # ===== Updated Weights =====
    w_embedding   = 0.18
    w_ast         = 0.10
    w_statistical = 0.15
    w_pattern     = 0.10
    w_linguistic  = 0.02   # CP code rarely has comments → remove noise
    w_behavior    = 0.45   

    final_score = (
        w_embedding   * scores.get("embedding_similarity", 0) +
        w_ast         * scores.get("ast_structural_score", 0) +
        w_statistical * scores.get("statistical_anomaly_score", 0) +
        w_pattern     * scores.get("pattern_score", 0) +
        w_linguistic  * scores.get("linguistic_score", 0) +
        w_behavior    * scores.get("behavioral_score", 0)
    )

    # Confidence
    confidence = abs(final_score - 0.5) * 2
    confidence = min(confidence, 1)

    # Thresholds tuned for CP
    if final_score >= 0.60:
        verdict = "AI"
    elif final_score <= 0.35:
        verdict = "Human"
    else:
        verdict = "Uncertain"

    return {
        "verdict": verdict,
        "confidence": confidence,
        "final_score": final_score
    }
