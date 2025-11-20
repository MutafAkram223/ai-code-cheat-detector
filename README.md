# AI-Cheat-Detector (C++) — Demo

This repository implements an academic/demo system for detecting AI-generated C++ competitive programming solutions.

## Features
- Streamlit UI with embedded Ace editor
- Multi-signal detection: embeddings, structural heuristics, statistical metrics, pattern heuristics, basic behavioral heuristics
- Modular code: agents + classifiers
- Runs locally with free tools

## Quick start
1. Create and activate a Python 3.10+ virtualenv.
2. `pip install -r requirements.txt`
3. Run: `streamlit run app.py`
4. Use "Start Coding" when you begin and "Submit Code" when finished.

## Notes
- This is a demo / educational system. Not production forensic tool.
- To improve detection, add real AI sample generation via HuggingFace/Gemini APIs (requires API keys).
- Keystroke-level behavior capture can be added via custom Streamlit components and JS.
