# app.py
import streamlit as st
from streamlit_ace import st_ace
import time
import os
import pandas as pd
import matplotlib.pyplot as plt

from src.utils.file_utils import ensure_dirs, save_json
from src.agents.problem_parser import parse_problem
from src.agents.real_ai_generator_agent import generate_ai_samples_for_problem
from src.agents.embedding_agent import compute_embedding_scores
from src.agents.ast_analyzer_agent import analyze_structure
from src.agents.statistical_agent import compute_statistical_scores
from src.agents.pattern_detector_agent import detect_patterns
from src.agents.nlp_feature_agent import analyze_comments
from src.agents.behavioral_agent import analyze_behavior_events
from src.classifiers.ensemble_classifier import compute_final_decision
from src.decision_agent import explain_decision


# ---------- CONFIG ----------
DATA_DIR = "data"
LOGS_DIR = os.path.join(DATA_DIR, "logs")
AI_SAMPLES_DIR = os.path.join(DATA_DIR, "ai_samples")
ensure_dirs([DATA_DIR, LOGS_DIR, AI_SAMPLES_DIR])


# ---------- Streamlit ----------
st.set_page_config(page_title="AI Cheat Detector (C++)", layout="wide")
st.title("Competitive Programming Code Cheating Detection (C++)")
st.markdown("""
This system evaluates whether a submitted C++ solution is **AI-generated** or **human-written**.
""")


# ---------- Session State ----------
if "events" not in st.session_state:
    st.session_state["events"] = []

if "last_code" not in st.session_state:
    st.session_state["last_code"] = ""

if "started_at" not in st.session_state:
    st.session_state["started_at"] = None

if "last_event_time" not in st.session_state:
    st.session_state["last_event_time"] = None


# ---------- Layout ----------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("Problem Statement")
    problem_text = st.text_area("Paste problem here", height=180)

    st.subheader("C++ Code Editor")
    editor_mode = st.selectbox("Editor theme", ["github", "monokai", "textmate"], index=0)

    initial_code = "// Type your C++ solution here\n#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    return 0;\n}\n"

    code = st_ace(
        value=st.session_state["last_code"] or initial_code,
        language="cpp",
        theme=editor_mode,
        key="ace_editor",
        height=420,
        auto_update=True,
    )

    submit = st.button("Submit Code")

with col2:
    st.subheader("Recent Runs")
    history_files = sorted(
        [f for f in os.listdir(LOGS_DIR) if f.endswith(".json")],
        reverse=True
    )
    if history_files:
        for f in history_files[:6]:
            st.write(f"- {f}")
    else:
        st.write("No runs available.")


# ---------- EVENT TRACKING ----------
now = time.time()

if st.session_state["started_at"] is None and code.strip() != "":
    st.session_state["started_at"] = now
    st.session_state["last_event_time"] = now

    init_len = len(code)
    st.session_state["events"].append({
        "t": now,
        "len": init_len,
        "delta": init_len,
        "interval": 0.0
    })
    st.session_state["last_code"] = code

if code != st.session_state["last_code"]:
    prev_len = len(st.session_state["last_code"])
    cur_len = len(code)
    delta = cur_len - prev_len
    interval = now - (st.session_state["last_event_time"] or now)

    st.session_state["events"].append({
        "t": now,
        "len": cur_len,
        "delta": delta,
        "interval": interval
    })

    st.session_state["last_code"] = code
    st.session_state["last_event_time"] = now


# ---------- SUBMIT LOGIC ----------
if submit:

    code_text = code or ""
    start = st.session_state["started_at"]
    total_time = (now - start) if start else None

    # ========== BEHAVIOR ANALYSIS ==========
    behavior_report = analyze_behavior_events(
        st.session_state["events"],
        total_time=total_time,
        code_text=code_text
    )

    # ========== RESET SESSION AFTER SUBMIT ==========
    st.session_state["events"] = []
    st.session_state["last_code"] = ""
    st.session_state["started_at"] = None
    st.session_state["last_event_time"] = None

    # ========== RUN NAME ==========
    timestamp = int(time.time())
    run_name = f"run_{timestamp}"
    run_dir = os.path.join(LOGS_DIR, run_name)
    os.makedirs(run_dir, exist_ok=True)

    # Save files
    with open(os.path.join(run_dir, "problem.txt"), "w") as f:
        f.write(problem_text)
    with open(os.path.join(run_dir, "solution.cpp"), "w") as f:
        f.write(code_text)

    # ========== PIPELINE ==========
    problem_features = parse_problem(problem_text)
    ai_sample_paths = generate_ai_samples_for_problem(problem_text, run_dir, num=3)
    embedding_result = compute_embedding_scores(code_text, ai_sample_paths)
    ast_metrics = analyze_structure(code_text)
    stat_metrics = compute_statistical_scores(code_text)
    pattern_metrics = detect_patterns(code_text)
    nlp_metrics = analyze_comments(code_text)

    behavior_score_struct = {
        "behavioral_score": behavior_report["behavioral_score"]
    }

    all_scores = {
        "embedding_similarity": embedding_result.get("similarity_score", 0.0),
        "ast_structural_score": ast_metrics.get("ast_score", 0.0),
        "statistical_anomaly_score": stat_metrics.get("stat_score", 0.0),
        "pattern_score": pattern_metrics.get("pattern_score", 0.0),
        "linguistic_score": nlp_metrics.get("linguistic_score", 0.0),
        "behavioral_score": behavior_score_struct["behavioral_score"],
    }

    result = compute_final_decision(all_scores)

    save_json(os.path.join(run_dir, "run_log.json"), {
        "timestamp": timestamp,
        "problem_features": problem_features,
        "ai_sample_paths": ai_sample_paths,
        "embedding_result": embedding_result,
        "ast_metrics": ast_metrics,
        "stat_metrics": stat_metrics,
        "pattern_metrics": pattern_metrics,
        "nlp_metrics": nlp_metrics,
        "behavior_report": behavior_report,
        "all_scores": all_scores,
        "final_result": result
    })

    # ========== OUTPUT ==========
    st.subheader("Detection Result")
    st.metric("Verdict", result["verdict"], f"{result['confidence']*100:.1f}%")

    # === CHEAT PROBABILITY CHART ===
    st.write("### Cheating Probability Chart")

    fig, ax = plt.subplots(figsize=(6, 1.4))

    prob = result["final_score"]
    color = "red" if prob >= 0.60 else "orange" if prob >= 0.40 else "green"

    ax.barh(["Cheat Probability"], [prob], color=color)
    ax.set_xlim(0, 1)
    ax.set_xlabel("0 = Human    |    1 = AI")
    ax.set_title("Cheating Likelihood Score")
    ax.grid(axis='x', linestyle='--', alpha=0.4)

    st.pyplot(fig)

    # === SIGNAL SCORES ===
    st.write("### Signal Scores")
    st.write(pd.DataFrame({
        "signal": list(all_scores.keys()),
        "score": [round(v, 4) for v in all_scores.values()]
    }))

    st.write("### Explanation")
    st.markdown(explain_decision(result, all_scores))

    st.success("Run complete.")
