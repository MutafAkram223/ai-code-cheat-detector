# src/agents/behavioral_agent.py

from statistics import mean

def analyze_behavior_events(events, paste_lengths, total_time, code_text):
    """
    Robust behavioral detector:
    - Uses sliding time-window aggregation of positive deltas to detect paste.
    - Returns dict with behavioral_score and debug info.
    """

    # Default (human)
    report = {
        "behavioral_score": 0.05,
        "debug": {
            "total_inserted": 0,
            "total_time": total_time,
            "max_window_chars": 0,
            "window_seconds": 0.5,
            "paste_lengths": paste_lengths,
        }
    }

    if not events:
        return report

    # Keep only positive insert events with timestamps
    insert_events = [(ev["t"], ev["delta"]) for ev in events if ev.get("delta", 0) > 0]
    if not insert_events:
        return report

    # Totals
    total_inserted = sum(d for (_, d) in insert_events)
    report["debug"]["total_inserted"] = total_inserted

    # Sliding window: compute max characters added within any window_seconds window
    window_seconds = 0.5
    report["debug"]["window_seconds"] = window_seconds

    times = [t for (t, _) in insert_events]
    deltas = [d for (_, d) in insert_events]

    max_window_sum = 0
    n = len(insert_events)
    j = 0
    current_sum = 0

    # two-pointer sliding window (events sorted by time)
    for i in range(n):
        t_i = times[i]
        current_sum += deltas[i]
        # move left pointer j while window exceeds window_seconds
        while j <= i and (t_i - times[j]) > window_seconds:
            current_sum -= deltas[j]
            j += 1
        if current_sum > max_window_sum:
            max_window_sum = current_sum

    report["debug"]["max_window_chars"] = max_window_sum

    # Also check if paste_lengths heuristic captured anything
    if paste_lengths:
        report["debug"]["paste_lengths"] = paste_lengths
        if max(paste_lengths) >= 80:
            report["behavioral_score"] = 1.0
            return report

    # RULES (final, simple and stable)
    # Hard paste: large burst within window_seconds
    if max_window_sum >= 80:
        report["behavioral_score"] = 1.0
        return report

    # Medium paste (suspicious)
    if max_window_sum >= 40:
        report["behavioral_score"] = 0.60
        return report

    # Fallback: small overall paste within entire session (fast total insertion)
    if total_inserted >= 150 and (total_time is not None) and total_time <= 0.6:
        report["behavioral_score"] = 1.0
        return report

    # Otherwise treat as human
    report["behavioral_score"] = 0.05
    return report
