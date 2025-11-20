# src/agents/behavioral_agent.py

from statistics import mean

def analyze_behavior_events(events, total_time=None, code_text=""):
    """
    Strong behavioral detection:
    - paste = 1.0
    - medium suspicious = 0.85
    - high typing speed = 0.65
    - normal human typing = 0.10 - 0.20
    - neutral = 0.35
    """

    report = {
        "behavioral_score": 0.50,
    }

    if not events:
        report["behavioral_score"] = 0.50
        return report

    inserts = []
    deletes = []
    speeds = []

    # gather statistics
    for ev in events:
        delta = ev["delta"]
        interval = ev["interval"] or 0.0001

        if delta > 0:
            inserts.append((delta, interval))
            speeds.append(delta / interval)
        elif delta < 0:
            deletes.append(abs(delta))

    # =============== 1. Strong PASTE detection ===============
    for (delta, interval) in inserts:
        if delta >= 40 and interval <= 2.0:
            report["behavioral_score"] = 1.0
            return report

    # First event cheat detector
    first_ev = events[0]
    if first_ev["len"] >= 100 and first_ev["interval"] <= 2.0:
        report["behavioral_score"] = 1.0
        return report

    # =============== 2. Medium suspicious ===============
    for (delta, interval) in inserts:
        if delta >= 20 and interval <= 1.0:
            report["behavioral_score"] = 0.85
            return report

    # =============== 3. Typing speed signals ===============
    avg_speed = mean(speeds) if speeds else 0

    # High typing speed (AI-like)
    if avg_speed >= 20:
        report["behavioral_score"] = 0.65
        return report

    # =============== 4. Human-like behavior ===============
    # human edits have deletes & slower varied speed
    total_deletes = sum(deletes)
    total_inserts = sum(delta for (delta, _) in inserts)

    if total_deletes > 0:
        # Humans revise code. AI rarely deletes.
        ratio = total_deletes / (total_inserts + 1)
        if ratio > 0.20:
            # Very Human
            report["behavioral_score"] = 0.15
            return report

    # Slow & deliberate typing
    if avg_speed < 10:
        report["behavioral_score"] = 0.20
        return report

    # =============== 5. Neutral typing ===============
    report["behavioral_score"] = 0.35
    return report
