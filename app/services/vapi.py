import requests
from typing import Dict, Any

def create_agent_vapi(token: str, agent_config: Dict[str, Any]):
    return {
        "agent_id": "vapi-agent-id-123",
        "message": "Agent created successfully using VAPI."
    }
