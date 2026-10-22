"""Agent Chaos Injection & Resilience Evaluator.
100% Python Standard Library.
"""

class AgentChaosResilienceEvaluator:
    """Evaluates agent trajectory resilience against simulated network faults, truncated tokens, and latency spikes."""

    @staticmethod
    def evaluate_resilience(trials: list) -> dict:
        recovered = 0
        total = len(trials)
        failure_modes = {}

        for t in trials:
            fault_type = t.get("injected_fault", "none")
            handled = bool(t.get("agent_recovered", False))
            if handled:
                recovered += 1
            else:
                failure_modes[fault_type] = failure_modes.get(fault_type, 0) + 1

        resilience_score = round((recovered / max(1, total)) * 100.0, 1)
        tier = "PRODUCTION_RESILIENT" if resilience_score >= 80.0 else ("DEGRADED" if resilience_score >= 50.0 else "UNSTABLE")

        return {
            "total_trials": total,
            "recovered_trials": recovered,
            "resilience_score": resilience_score,
            "resilience_tier": tier,
            "unhandled_faults": failure_modes
        }
