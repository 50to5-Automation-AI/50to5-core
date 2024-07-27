from typing import List, Dict, Any, Optional, Tuple
from agentprotocol.chat import GroupChatManager, ChatResult
from agentprotocol.api import createAgentTask, listAgentTasks, getAgentTask, executeAgentTaskStep, listAgentTaskArtifacts, uploadAgentTaskArtifacts

class GroupManagerAgent(GroupChatManager):
    def __init__(self, state: Dict[str, Any]):
        super().__init__()
        self.state = state  # Holds the current state of tasks and priorities
        self.priority_queue = []  # A queue to manage task priorities

    def ingest_initial_state(self, goals: Dict[str, Any], engineering_repo: Dict[str, Any], marketing_repo: Dict[str, Any]):
        self.state['goals'] = goals
        self.state['engineering_tasks'] = engineering_repo
        self.state['marketing_tasks'] = marketing_repo
        self.update_priority_queue()

    def update_priority_queue(self):
        all_tasks = self.state['engineering_tasks'] + self.state['marketing_tasks']
        self.priority_queue = sorted(all_tasks, key=lambda task: task['priority'], reverse=True)

    def create_task_in_jira(self, task_details: Dict[str, Any]) -> str:
        response = createAgentTask({
            "input": f"Create a new task in Jira with details: {task_details}",
            "additional_input": task_details
        })
        return response['task_id']

    def create_task_in_clickup(self, task_details: Dict[str, Any]) -> str:
        response = createAgentTask({
            "input": f"Create a new task in ClickUp with details: {task_details}",
            "additional_input": task_details
        })
        return response['task_id']

    def sync_tasks(self):
        jira_tasks = listAgentTasks({"project": "JiraProjectKey"})
        clickup_tasks = listAgentTasks({"project": "ClickUpProjectKey"})
        self.state['engineering_tasks'] = jira_tasks['tasks']
        self.state['marketing_tasks'] = clickup_tasks['tasks']
        self.update_priority_queue()

    def prioritize_tasks(self):
        self.update_priority_queue()
        highest_priority_task = self.priority_queue[0] if self.priority_queue else None
        return highest_priority_task

    def decide_who_to_speak_to(self, task: Dict[str, Any]):
        if 'jira' in task['source']:
            return 'Engineering'
        elif 'clickup' in task['source']:
            return 'Marketing'
        return 'Both'

    def manage_group_chat(self):
        highest_priority_task = self.prioritize_tasks()
        if highest_priority_task:
            team = self.decide_who_to_speak_to(highest_priority_task)
            if team == 'Engineering':
                self.speak_to_engineering(highest_priority_task)
            elif team == 'Marketing':
                self.speak_to_marketing(highest_priority_task)
            else:
                self.speak_to_both_teams(highest_priority_task)

    def speak_to_engineering(self, task: Dict[str, Any]):
        messages = [{"role": "system", "content": f"Discuss the following task with the Engineering team: {task}"}]
        self.run_chat(messages=messages, sender=self, config=self.groupchat)

    def speak_to_marketing(self, task: Dict[str, Any]):
        messages = [{"role": "system", "content": f"Discuss the following task with the Marketing team: {task}"}]
        self.run_chat(messages=messages, sender=self, config=self.groupchat)

    def speak_to_both_teams(self, task: Dict[str, Any]):
        messages = [{"role": "system", "content": f"Discuss the following task with both teams: {task}"}]
        self.run_chat(messages=messages, sender=self, config=self.groupchat)

    def maintain_state(self):
        self.sync_tasks()
        self.update_priority_queue()

    def clear_task_history(self, task_id: str):
        clear_agents_history({"input": "clear history"}, self.groupchat)

    def add_artifact(self, task_id: str, artifact_details: Dict[str, Any]):
        uploadAgentTaskArtifacts(task_id, artifact_details)

    def get_task_artifacts(self, task_id: str):
        return listAgentTaskArtifacts(task_id)

    def resume_group_chat(self, messages: Union[List[Dict], str]):
        self.resume(messages=messages, remove_termination_string="clear history")

    def save_state(self):
        return self.state

    def load_state(self, state: Dict[str, Any]):
        self.state = state
        self.update_priority_queue()

# Example usage
state = {}
manager_agent = GroupManagerAgent(state)
goals = {"objective": "Improve cross-team collaboration"}
engineering_repo = [{"task_id": "ENG1", "priority": 1, "source": "jira"}]
marketing_repo = [{"task_id": "MKT1", "priority": 2, "source": "clickup"}]

manager_agent.ingest_initial_state(goals, engineering_repo, marketing_repo)
manager_agent.manage_group_chat()
