'''
JSON Agent: This agent will ensure that the final out put of all agents is structured json
'''
import json
import autogen
import yaml

proxy_agent = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    code_execution_config=False,
    system_message="Reply in JSON. Only JSOn",
    default_auto_reply="",
    description="""This agent is the user. Your job is to get an anwser from the agent groups back to this user agent. Respond in JSON""",
    is_termination_msg=lambda x: True,
)

allowed_transitions = {
    proxy_agent: [IO_Agent],
    IO_Agent: [friendly_agent, suspicious_agent],
    suspicious_agent: [proxy_agent],
    friendly_agent: [proxy_agent],
}


