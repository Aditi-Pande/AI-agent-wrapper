from pydantic import BaseModel
from typing import Any, Dict

class AgentConfig(BaseModel):
    llm_id: str
    voice_id: str

class CreateAgentRequest(BaseModel):
    provider: str
    token: str
    agent_config: AgentConfig

class CreateAgentResponse(BaseModel):
    agent_id: str
    provider: str
    message: str
