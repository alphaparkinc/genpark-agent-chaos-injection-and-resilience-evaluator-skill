"""Example usage for Agent Chaos Injection & Resilience Evaluator."""
from client import AgentChaosResilienceEvaluator

if __name__ == "__main__":
    trials = [
        {"injected_fault": "timeout_3s", "agent_recovered": True},
        {"injected_fault": "http_429", "agent_recovered": True},
        {"injected_fault": "dns_failure", "agent_recovered": False}
    ]
    res = AgentChaosResilienceEvaluator.evaluate_resilience(trials)
    print("Resilience Tier:", res["resilience_tier"], "Score:", res["resilience_score"])
