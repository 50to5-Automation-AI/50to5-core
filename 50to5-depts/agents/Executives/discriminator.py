from agentchat.assistant_agent import AssistantAgent

class DiscriminatorAgent(AssistantAgent):
    def __init__(self, name: str, system_message: str):
        super().__init__(name=name, system_message=system_message)
        # Additional initialization if needed

    def ask_hard_questions(self, tasks: List[Dict]):
        """Ask challenging questions to improve task generation and allocation."""
        # Logic to ask hard questions
        pass