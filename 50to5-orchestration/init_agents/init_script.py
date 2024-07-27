import yaml
import psycopg2
from typing import Dict, Any

# Department Agent class definition
class DepartmentAgent:
    def __init__(self, name: str, description: str, db_config: Dict[str, Any], roles: list, tasks: list, metrics: list):
        self.name = name
        self.description = description
        self.db_config = db_config
        self.roles = roles
        self.tasks = tasks
        self.metrics = metrics
        self.connect_db()

    def connect_db(self):
        self.conn = psycopg2.connect(**self.db_config)
        self.cursor = self.conn.cursor()

    def perform_task(self, task):
        print(f"{self.name} performing task: {task}")

    def monitor_metrics(self):
        print(f"{self.name} monitoring metrics: {self.metrics}")

# Load configuration
def load_config(config_file: str) -> Dict[str, Any]:
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Instantiate agents
def instantiate_agents(config: Dict[str, Any]):
    agents = []
    for department in config['departments']:
        agent = DepartmentAgent(
            name=department['name'],
            description=department['description'],
            db_config=department['db_config'],
            roles=department['roles'],
            tasks=department['tasks'],
            metrics=department['metrics']
        )
        agents.append(agent)
    return agents

# Main function
def main():
    config_file = 'department_config.yaml'
    config = load_config(config_file)
    agents = instantiate_agents(config)
    
    # Example usage
    for agent in agents:
        agent.perform_task(agent.tasks[0])
        agent.monitor_metrics()

if __name__ == "__main__":
    main()
