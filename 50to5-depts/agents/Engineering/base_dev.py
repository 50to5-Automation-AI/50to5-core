import os
import autogen
from autogen import AssistantAgent, UserProxyAgent, 
from pydantic import BaseModel
from ..base_agent import BaseAgent

class EngineeringAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        # Add any specific initializations for the Engineering agent