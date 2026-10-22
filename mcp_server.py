"""MCP server for Agent Chaos Injection & Resilience Evaluator."""
import sys
import json
from client import AgentChaosResilienceEvaluator

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "evaluate_chaos_resilience",
                "description": "Evaluates agent recovery rates across injected fault trials",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "trials": {"type": "array"}
                    },
                    "required": ["trials"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "evaluate_chaos_resilience":
            trials = params.get("arguments", {}).get("trials", [])
            res = AgentChaosResilienceEvaluator.evaluate_resilience(trials)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
